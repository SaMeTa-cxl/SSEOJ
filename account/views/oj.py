from django.contrib import auth
from marshmallow import ValidationError
from rest_framework.views import APIView

from ..models import User
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
        pass


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
        pass


class UserFollowingAPI(APIView):
    def get(self, request, user_id):
        pass


class UserFollowerAPI(APIView):
    def get(self, request, user_id):
        pass


class UserInfoChangeAPI(APIView):
    def put(self, request):
        pass


class UserAvatarChangeAPI(APIView):
    def put(self, request):
        pass


class UserProblemlistAPI(APIView):
    def get(self, request, user_id):
        pass
