from rest_framework.views import APIView


class ProblemDescriptionAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemSolutionsAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemSolutionsDetailAPI(APIView):
    def get(self, request, problem_id, solution_id):
        pass


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemListAPI(APIView):
    def get(self, request):
        pass


class ProblemListDetaiAPI(APIView):
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
