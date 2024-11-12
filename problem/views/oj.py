from rest_framework.views import APIView

from problem.models import Problem, Solution
from problem.serializers import ProblemSerializer, SolutionSerializer
from utils.api import success


class ProblemDescriptionAPI(APIView):
    @staticmethod
    def get(request, problem_id):
        problem = Problem.objects.get(id=problem_id)
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
        problem = Problem.objects.get(id=problem_id)
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
