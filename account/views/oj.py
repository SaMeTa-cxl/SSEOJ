from django.contrib import auth
from rest_framework.views import APIView

from ..serializers import UserLoginSerializer
from utils.api import *


class UserLoginApi(APIView):
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


class UserLogoutApi(APIView):
    def get(self, request):
        """
        GET /api/logout
        """
        auth.logout(request)
        return Response()
