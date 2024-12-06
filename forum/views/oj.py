from rest_framework.views import APIView


class PostInformationAPI(APIView):
    def get(self, request, problem_id):
        pass


class PostCommentInformation(APIView):
    def get(self, request, problem_id):
        pass


class PostCommentNew(APIView):
    def post(self, request, problem_id):
        pass


class PostNew(APIView):
    def post(self, request, problem_id):
        pass


class PostGood(APIView):
    def put(self, request, problem_id):
        pass
