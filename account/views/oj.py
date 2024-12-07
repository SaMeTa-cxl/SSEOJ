from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from ..models import User, Following
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
        password = data.get('password')
        verificationCode = data.get('verification_code')

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
        user = auth.authenticate(email=data.get('email'), password=data.get('password'))

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
    def get(self, request, id):
        try:
            userInfo = User.objects.get(id = id)
        except User.DoesNotExist:
            return fail(msg= "用户不存在")

        Rserializer = UserInfoSerializer(userInfo)
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
    def get(self, request, user_id):
        if not request.user.is_authenticated:
            return fail(msg = "未登录")



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

        user.avatar = ImageCode.base64_image(avatar, user.id)
        user.save()

        return success("修改成功")

class UserPasswordChangeAPI(APIView):
    def put(self, request):
        data = request.data
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return fail(msg = "User not found")

        if not request.user.is_authenticated:
            return fail(msg = "No permission to change")
        elif request.user.id != data["user_id"]:
            return fail(msg = "No permission to change")

        user.set_password(data["password"])
        user.save()

        return success("success")

class UserPasswordForgetAPI(APIView):
    def put(self, request):
        pass

class CreatProblemListAPI(APIView):
    def get(self, request):
        pass

class EditProblemListAPI(APIView):
    def put(self, request, problemlist_id):
        pass

class GetTryProblemAPI(APIView):
    def get(self, request, user_id):
        pass

class StarProblemAPI(APIView):
    def get(self, request, user_id):
        pass
