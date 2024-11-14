from django.db.models import Q
from rest_framework.views import APIView

from problem.models import Problem, Solution, ProblemList
from problem.serializers import ProblemSerializer, SolutionSerializer, ProblemListSerializer, \
    ProblemListDetailSerializer
from utils.api import success, fail, paginate_data


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
    @staticmethod
    def get(request, problem_id, solution_id):
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        try:
            solution = problem.solutions.get(id=solution_id)
        except Solution.DoesNotExist:
            return fail('该题解不存在')

        return success(solution.content)


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemListAPI(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword', '')
        problem_lists = ProblemList.objects.filter((Q(title__icontains=keyword) | Q(summary__icontains=keyword))
                                                   & Q(is_deleted=False) & Q(is_public=True))
        response_data = paginate_data(request, problem_lists, ProblemListSerializer)
        if not request.user.is_authenticated:
            for problem_list in response_data:
                problem_list['pass_count'] = None
            return success(response_data)

        problem_lists = problem_lists.exclude(create_user=request.user)
        # response_data为list,problem_list为字典
        for problem_list in response_data:
            problem_list['pass_count'] = 0
            for problem in problem_lists[problem_list['id'] - 1].problems.all():
                if problem.get_pass_status(request.user):
                    problem_list['pass_count'] += 1

        return success(response_data)


class ProblemListDetailAPI(APIView):
    def get(self, request, problemlist_id):
        if not request.user.is_authenticated:
            return fail("用户未登录！")
        try:
            problem_list = ProblemList.objects.get(id=problemlist_id)
        except ProblemList.DoesNotExist:
            return fail("该题单不存在！")

        response_data = ProblemListDetailSerializer(problem_list).data
        response_data['star_status'] = problem_list.get_star_status(request.user)
        problems = response_data['problems']
        for problem in problems:
            problem['pass_status'] = Problem.objects.get(id=problem['id']).get_pass_status(request.user)

        return success(response_data)


class ProblemListStarAPI(APIView):
    def post(self, request):
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
