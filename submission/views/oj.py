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
                                               username=request.user.username,
                                               language=data["language"],
                                               problem=problem,
                                               code=data["submitted_code"]
                                               )
        # use this for debug
        # JudgeDispatcher(submission.id, problem.id).judge()
        judge_task.send(submission.id, problem.id)

        success_data = {}
        if submission.result != JudgeStatus.COMPILE_ERROR:
            success_data["problem_status"] = "AC" if submission.result == JudgeStatus.ACCEPTED else "RJ"
            success_data["submit_id"] = submission.id
            success_data["submit_time"] = submission.create_time
            total_time_spent = 0
            max_space_spent = 0
            for object in submission.info:
                total_time_spent += object["real_time"]
                max_space_spent += max(object["memory"], max_space_spent)
            success_data["time_spent"] = total_time_spent
            success_data["space_spent"] = max_space_spent
            success_data["language"] = submission.language
        else:   #编译未通过则submission.info中只有err和data字段
            success_data["problem_status"] = "RJ"
            success_data["submit_id"] = submission.id
            success_data["submit_time"] = submission.create_time
            success_data["time_spent"] = None
            success_data["space_spent"] = None
            success_data["language"] = submission.language

        return success(success_data)
