from rest_framework.views import APIView
from problem.models import Problem
from utils.api import *
from submission.models import Submission, JudgeStatus
from judge.tasks import judge_task


class ProblemSubmissionsAPI(APIView):
    def get(self, request, problem_id):
        if not request.user.is_authenticated:
            return fail("用户未验证")
        user_id = request.user.id
        status = request.query_params.get('status')
        language = request.query_params.get('language')
        sort_type = request.query_params.get('sort_type')

        filter_conditions = {'problem_id': problem_id, 'user_id': user_id}
        if status:
            filter_conditions['status'] = status
        if language:
            filter_conditions['language'] = language

        submissions = Submission.objects.filter(**filter_conditions)
        if sort_type:
            if sort_type == "time":
                submissions = submissions.order_by("-create_time")
            elif sort_type == "optimal":
                submissions = submissions.order_by("time_spent", "memory_spent")

        submission_data = []
        for submission in submissions:
            tmp_dict = {}
            tmp_dict['submit_time'] = submission.created_time
            tmp_dict['code'] = submission.code
            tmp_dict['language'] = submission.language
            tmp_dict['result'] = submission.result
            tmp_dict['error_info'] = submission.error_info
            tmp_dict['time_spent'] = submission.time_spent
            tmp_dict['memory_spent'] = submission.memory_spent
            submission_data.append(tmp_dict)
        return success(submission_data)

class ProblemSubmitAPI(APIView):
    def post(self, request):
        data = request.data

        try:
            problem = Problem.objects.get(id=data["problem_id"])
        except Problem.DoesNotExist:
            return fail("题目不存在")

        submission = Submission.objects.create(user_id=request.user.id,
                                               language=data["language"],
                                               problem=problem,
                                               code=data["submitted_code"]
                                               )
        # use this for debug
        # JudgeDispatcher(submission.id, problem.id).judge()
        judge_task.send(submission.id, problem.id)

        return success("成功")
