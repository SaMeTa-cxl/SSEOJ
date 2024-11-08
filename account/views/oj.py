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


class UserSendEmailAPI(APIView):
    def get(self, request):
        pass


class UserRegisterAPI(APIView):
    def post(self, request):
        pass


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
