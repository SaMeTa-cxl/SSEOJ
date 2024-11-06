from django.contrib import auth

from utils.api.api import APIView, validate_serializer
from ..serializers import UserLoginSerializer


class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        """
        POST /api/login
        """
        data = request.data
        user = auth.authenticate(username=data['username'], password=data['password'])
        if not user:
            return self.error("用户名或密码错误！")
        else:
            auth.login(request, user)
            return self.success("登录成功")


class UserLogoutAPI(APIView):
    def get(self, request):
        """
        GET /api/logout
        """
        auth.logout(request)
        return self.success()