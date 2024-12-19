from rest_framework.views import APIView
from problem.models import Problem
from utils.api import *
from submission.models import Submission, JudgeStatus
from judge.tasks import judge_task


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        pass


class ProblemSubmitAPI(APIView):
    def post(self, request):
        data = request.data

        try:
            problem = Problem.objects.get(id=data["problem_id"])
        except Problem.DoesNotExist:
            return fail("Problem not exist")

        submission = Submission.objects.create(user_id=request.user.id,
                                               language=data["language"],
                                               problem=problem,
                                               code=data["submitted_code"]
                                               )
        # use this for debug
        # JudgeDispatcher(submission.id, problem.id).judge()
        judge_task.send(submission.id, problem.id)

        return success("success")
