from django.contrib import auth
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sympy import Integer

from problem.models import ProblemList, StudyPlan
from problem.serializers import ProblemSerializer
from submission.models import Submission, JudgeStatus
from ..models import *
from ..serializers import *
from utils.api import *
from django.core.cache import cache
from utils.api import ImageCode, VerificationCode, DecodePassword
from django.contrib.sessions.models import Session


class EmailCodeAPI(APIView):
    def post(self, request):
        data = request.data
        try:
            requestType = int(data.get('type'))
        except ValueError:
            requestType = 0

        toEmail = data.get('email')

        if requestType == 0:
            if request.user.is_authenticated:
                return fail(msg = '已登录无法获取注册验证码')

            if User.objects.filter(email=toEmail).exists():
                return fail(msg='该邮箱已注册')

            code = VerificationCode.sendMessage(toEmail, 0)
            if code is None:
                return fail(msg = "发送失败")

            cache.set(toEmail, code, timeout=300)
            return success('发送成功')

        elif requestType == 1:
            try:
                user = User.objects.get(email=toEmail)
            except User.DoesNotExist:
                return fail(msg = '该邮箱不存在')

            if user.email != toEmail:
                return fail(msg = "邮箱错误")

            code = VerificationCode.sendMessage(toEmail, 1)
            if code is None:
                return fail(msg = "发送失败")

            cache.set(toEmail, code, timeout=10)
            return success('发送成功')

        else:
            return fail(msg = "未知的申请类型")


class UserRegisterAPI(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')
        password = DecodePassword.decryption(data.get('password'))
        verificationCode = data.get('verification_code')
        print(data)

        if not email or not username or not password:
            return fail(msg = "所有字段均为必填项")
        if User.objects.filter(email=email).exists():
            return fail(msg = "该邮箱已注册")

        if verificationCode != cache.get(email):
            return fail(msg='验证码错误或过期')
        else:
            cache.delete(email)

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.full_clean()
            user.save()

            avatar = ImageCode.image_base64(user.avatar)
            data = UserLogInformation(user).data
            data['avatar'] = avatar
            return success(data)
        except Exception:
            return fail(msg='注册失败')


class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        data = request.data
        user = auth.authenticate(email=data.get('email'), password=DecodePassword.decryption(data.get('password')))

        if not user:
            return fail(msg = "邮箱或密码错误")
        else:
            auth.login(request, user)
            avatar = ImageCode.image_base64(user.avatar)
            data = UserLogInformation(user).data
            data['avatar'] = avatar
            return success(data)


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return success("退出成功")


class UserInfoAPI(APIView):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, id):
        user = request.user

        try:
            userInfo = User.objects.get(id = id)
        except User.DoesNotExist:
            return fail(msg= "用户不存在")

        Rserializer = UserInfoSerializer(userInfo, context={'user': user})
        userData = Rserializer.data
        userData["avatar"] = ImageCode.image_base64(userInfo.avatar)
        #userData["subscribing_count"] = serializer.get_subscribing_count(userInfo)
        #userData["subscribers_count"] = serializer.get_subscribers_count(userInfo)

        return success(userData)


class UserSubscribeAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail(msg = "用户未登录")

        user_id = request.user.id
        following_user_id = request.data.get('id')
        relationship = request.data.get('relationship')

        if relationship not in ["0", "1"]:
            return fail(msg = "错误的关注状态")

        if user_id == following_user_id:
            return fail(msg = '不能关注自己')

        try:
            user = User.objects.get(id=user_id)
            following_user = User.objects.get(id=following_user_id)
        except User.DoesNotExist:
            return fail(msg = "不存在该用户")

        if relationship == "1":
            following_record, created = Following.objects.get_or_create(follower=user, following=following_user)
            return success("关注成功")
        else:
            Following.objects.filter(follower=user, following=following_user).delete()
            return success("取消关注成功")


class UserFollowingAPI(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return fail(msg = "没有找到该用户")

        myself = None
        if request.user.is_authenticated:
            myself = request.user

        following_records = Following.objects.filter(follower=user)
        following_user = []
        for record in following_records:
            following_user.append(record.following)

        Rserializer = UserFollowingSerializer(following_user, many=True, context={'myself': myself})

        """
        res = []
        for record in following_records:
            following_user = record.following

            is_following_me = False
            if myself:
                Following.objects.get(follower=following_user, following=myself).exists()

            is_followed_by_me = False
            if myself:
                Following.objects.get(follower=myself, following=following_user).exists()

            is_mutual_following = False
            if is_following_me and is_followed_by_me:
                is_mutual_following = True

            res.append(
                {
                    'id': following_user.id,
                    'username': following_user.username,
                    'profile': following_user.profile,
                    'is_mutual_following': is_mutual_following,
                    'is_following_me': is_following_me,
                    'is_followed_by_me': is_followed_by_me
                }
            )
        """

        return success(Rserializer.data)


class UserFollowerAPI(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return fail(msg = "没有找到该用户")

        myself = None
        if request.user.is_authenticated:
            myself = request.user

        following_records = Following.objects.filter(following=user)
        Rserializer = UserFollowingSerializer(following_records, many=True, context={'myself': myself})
        """
        res = []
        for record in following_records:
            following_user = record.following

            is_following_me = False
            if myself:
                Following.objects.get(follower=following_user, following=myself).exists()

            is_followed_by_me = False
            if myself:
                Following.objects.get(follower=myself, following=following_user).exists()

            is_mutual_following = False
            if is_following_me and is_followed_by_me:
                is_mutual_following = True

            res.append(
                {
                    'id': following_user.id,
                    'username': following_user.username,
                    'profile': following_user.profile,
                    'is_mutual_following': is_mutual_following,
                    'is_following_me': is_following_me,
                    'is_followed_by_me': is_followed_by_me
                }
            )
        """

        return success(Rserializer.data)


class StudyPlanAPI(APIView):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return fail(msg = "未登录")

        myself = request.user
        if myself.id != id:
            return fail(msg = '无权查看')

        plans = StudyPlan.objects.filter(Q(user = myself))
        for plan in plans:
            if not plan.problem_status:
                problem = plan.problem
                submissions = Submission.objects.filter(Q(problem = problem) & Q(user_id = myself.id))
                for sub in submissions:
                    if sub.result == JudgeStatus.ACCEPTED:
                        plan.problem_status = True
                        plan.save()
                        break

        data = GetStudyPlanSerializer(plans, many = True).data
        return success(data)


class UserProfileChangeAPI(APIView):
    def put(self, request):
        if not request.user.is_authenticated:
            return fail(msg = '未登录')

        user = request.user
        data = request.data

        user.profile = data.get('profile')
        user.save()
        return success("修改成功")


class UserNameChangeAPI(APIView):
    def put(self, request):
        if not request.user.is_authenticated:
            return fail(msg = "未登录")

        data = request.data
        user = request.user

        user.username = data.get("username")
        user.save()

        return success("修改成功")


class UserAvatarChangeAPI(APIView):
    def put(self, request):
        if not request.user.is_authenticated:
            return fail(msg = "未登录")

        user = request.user
        avatar = request.data.get("avatar")

        # 查找 'base64,' 的起始位置，并加1以包含逗号本身
        index = avatar.find('base64,') + len('base64,')
        # 使用切片获取 'base64,' 后面的部分
        avatar = avatar[index:]

        user.avatar = ImageCode.base64_image(avatar, user.id)
        user.save()

        return success("修改成功")


class UserPasswordChangeAPI(APIView):
    def put(self, request):
        if not request.user.is_authenticated:
            return fail(msg = '未登录')

        data = request.data
        user = request.user
        userId = -1
        passBefore = DecodePassword.decryption(data.get("password_before"))
        passNew = DecodePassword.decryption(data.get("password_new"))
        try:
            userId = int(data.get("id"))
        except ValueError:
            pass

        if user.id != userId:
            return fail(msg = '权限不足')

        if not user.check_password(passBefore):
            return fail(msg = '旧密码错误')

        user.set_password(passNew)

        return success('修改成功')


class UserPasswordForgetAPI(APIView):
    def put(self, request):
        data = request.data
        email = data.get('email')
        passNew = DecodePassword.decryption(data.get('password_new'))
        verificationCode = data.get('verification_code')

        if verificationCode != cache.get(email):
            return fail(msg='验证码错误或过期')
        else:
            cache.delete(email)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return fail(msg = '用户不存在')

        user.set_password(passNew)

        return success('修改成功')


class GetTryProblemAPI(APIView):
    def get(self, request, user_id):
        submissions = Submission.objects.filter(user_id=user_id)
        problems = []
        for submission in submissions:
            problems.append(submission.problem)
        problems = list(set(problems))
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return fail('用户不存在！')
        problems = [{
            'pass_status': problem.pass_users.contains(user),
            'id': problem.id,
            'name': problem.name,
            'difficulty': problem.difficulty,
        } for problem in problems]
        return success(problems)


class StarProblemAPI(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return fail('用户不存在！')
        return success(ProblemSerializer(user.star_problems,
                                         many=True,
                                         needed_fields=['id', 'name', 'difficulty',
                                                        'tags', 'pass_count', 'attempt_count']).data)


class UserProblemListAPI(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return fail('用户不存在！')
        if request.user != user:
            problem_lists = ProblemList.objects.filter(Q(create_user=user) & Q(is_public=True))
            return success(ProblemListSerializer(problem_lists, many=True).data)
        else:
            problem_lists = ProblemList.objects.filter(Q(create_user=user))
            return success(ProblemListSerializer(problem_lists, many=True).data)
