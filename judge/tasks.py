import dramatiq

from submission.models import Submission
from judge.dispatcher import JudgeDispatcher


@dramatiq.actor(time_limit=3600_000, max_retries=0, max_age=7200_000)
def judge_task(submission_id, problem_id):
    uid = Submission.objects.get(id=submission_id).user_id
    JudgeDispatcher(submission_id, problem_id).judge()
