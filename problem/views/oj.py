from rest_framework.views import APIView

from problem.models import Problem, Solution
from problem.serializers import ProblemSerializer, SolutionSerializer
from utils.api import success, fail


class ProblemDescriptionAPI(APIView):
    @staticmethod
    def get(request, problem_id):
        """
        获取id为problem_id的题目的详细信息，包括题目的所有字段信息和请求用户的pass_status和star_status
        注：当用户未登录时，pass_status、star_status均为None
        """
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        serializer = ProblemSerializer(problem)
        response_data = serializer.data
        response_data['similar_problems'] = problem.get_similar_problems(request.user)
        response_data['pass_status'] = problem.get_pass_status(request.user)
        response_data['star_status'] = problem.get_star_status(request.user)
        # print(response_data)
        return success(response_data)


class ProblemSolutionsAPI(APIView):
    @staticmethod
    def get(request, problem_id):
        """
        获取id为problem_id的题目的所有题解信息，其中详细内容被截断为最多200个字符
        返回为一个字典列表，每个字典为一个题解的信息
        """
        if not request.user.is_authenticated:
            return fail('用户未登录')
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        solutions = problem.solutions.all()
        print(SolutionSerializer(solutions, many=True).data)
        return success(SolutionSerializer(solutions, many=True).data)


class ProblemSolutionsDetailAPI(APIView):
    def get(self, request, problem_id, solution_id):
        pass


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemListAPI(APIView):
    def get(self, request):
        pass


class ProblemListDetailAPI(APIView):
    def get(self, request, problemlist_id):
        pass


class ProblemListStarAPI(APIView):
    def get(self, request):
        pass


class ProblemSubmitAPI(APIView):
    def post(self, request):
        pass


class ProblemSolutionCreateAPI(APIView):
    def post(self, request):
        pass


class ProblemsetAPI(APIView):
    def post(self, request):
        pass
