from django.contrib import auth
from marshmallow import ValidationError
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from ..models import User, Following
from ..serializers import UserLoginSerializer
from utils.api import *


class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        """
        POST /api/login
        """
        data = request.data
        user = auth.authenticate(email=data['email'], password=data['password'])
        if not user:
            return fail("用户名或密码错误！")
        else:
            auth.login(request, user)
            return success("登录成功")


class UserLogoutAPI(APIView):
    def get(self, request):
        """
        GET /api/logout
        """
        auth.logout(request)
        # return Response({"message": "登出成功"}, status=status.HTTP_200_OK)
        return success("登出成功")


class UserSendEmailAPI(APIView):
    def get(self, request):
        email = request.GET.get('email')
        user_id = request.GET.get('user_id', None)
        if user_id == None:
            user = auth.authenticate(email=email)
            if not user:    #用户未注册，使用邮箱验证码注册新账号
                return success({"verification_code": "999999"})
            else:   #用户已注册，使用邮箱验证码登录
                user_id = user.id
                return success({"verification_code": "888888", "user_id": user_id})

        else:   #用户已登录
            user = auth.authenticate(email=email, user_id=user_id)
            if not user:    #理论上不会出现
                return fail("用户状态异常！")
            else:   #用户已登录，使用邮箱验证码修改密码等
                return success({"verification_code": "777777", "user_id": user_id})



class UserRegisterAPI(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        if not email or not username or not password:
            return fail("所有字段均为必填项")
        if User.objects.filter(email=email).exists():
            return fail("该邮箱已注册")
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.full_clean()
            user.save()
            return success("注册成功！")
        except Exception as e:
            return fail(e)




class UserInfoAPI(APIView):
    def get(self, request, user_id):
        pass


class UserSubscribeAPI(APIView):
    def post(self, request):
        user_id = request.COOKIES.get('user_id')
        following_user_id = request.data.get('user_id')
        relationship = request.data.get('relationship')

        if relationship not in [0, 1]:
            return fail("Invalid relationship status")

        try:
            user = User.objects.get(user_id=user_id)
            following_user = User.objects.get(user_id=following_user_id)
        except User.DoesNotExist:
            raise NotFound("User or Following user does not exist")

        if relationship == 1:
            following_record, created = Following.objects.get_or_create(follower=user, following=following_user)
            return success("关注成功")
        else:
            Following.objects.filter(follower=user, following=following_user).delete()
            return success("取消关注成功")


class UserFollowingAPI(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found!")

        following_records = Following.objects.filter(follower=user)
        res = []
        for record in following_records:
            following_user = record.following
            is_mutual_following = Following.objects.get(follower=following_user, following=user).exists()
            is_following_me = is_mutual_following
            is_followed_by_me = True
            #后面这两个有点问题，目前写的只针对查看自己的关注列表

            res.append(
                {
                    'user_id': following_user.id,
                    'user_name': following_user.username,
                    'profile': following_user.profile,
                    'is_mutual_following': is_mutual_following,
                    'is_following_me': is_following_me,
                    'is_followed_by_me': is_followed_by_me
                }
            )
        return success(res)


class UserFollowerAPI(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found!")

        following_records = Following.objects.filter(following=user)
        res = []
        for record in following_records:
            following_user = record.following
            is_mutual_following = Following.objects.get(follower=user, following=following_user).exists()
            is_following_me = is_mutual_following
            is_followed_by_me = True
            # 后面这两个有点问题，目前写的只针对查看自己的粉丝列表

            res.append(
                {
                    'user_id': following_user.id,
                    'user_name': following_user.username,
                    'profile': following_user.profile,
                    'is_mutual_following': is_mutual_following,
                    'is_following_me': is_following_me,
                    'is_followed_by_me': is_followed_by_me
                }
            )
        return success(res)


class UserInfoChangeAPI(APIView):
    def put(self, request):
        pass


class UserAvatarChangeAPI(APIView):
    def put(self, request):
        pass


class UserProblemlistAPI(APIView):
    def get(self, request, user_id):
        pass
