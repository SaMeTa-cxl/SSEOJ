from django.contrib import auth
from rest_framework.views import APIView

from ..serializers import UserLoginSerializer
from utils.api import *


class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        """
        POST /api/login
        """
        data = request.data
        user = auth.authenticate(username=data['username'], password=data['password'])
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
        return Response()


class UserSendEmail(APIView):
    def get(self, request):
        pass


class UserRegister(APIView):
    def post(self, request):
        pass


class UserInfo(APIView):
    def get(self, request):
        pass


class UserSubscribe(APIView):
    def post(self, request):
        pass


class UserFollowing(APIView):
    def get(self, request):
        pass


class UserFollowers(APIView):
    def get(self, request):
        pass


class UserProfileChange(APIView):
    def put(self, request):
        pass


class UserAvatarChange(APIView):
    def put(self, request):
        pass


class UserPasswordChange(APIView):
    def put(self, request):
        pass


class UserNameChange(APIView):
    def put(self, request):
        pass


class UserFollower(APIView):
    def get(self, request):
        pass
