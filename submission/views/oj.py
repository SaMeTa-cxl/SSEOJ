from rest_framework.views import APIView
from utils.api import success, fail


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        if not request.user.is_authenticated:
            return fail(msg = '未登录')

        user = request.user
        

        pass


class ProblemSubmitAPI(APIView):
    def post(self, request):
        pass
