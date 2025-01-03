import dramatiq

from submission.models import Submission
from judge.dispatcher import JudgeDispatcher


@dramatiq.actor(time_limit=3600_000, max_retries=0, max_age=7200_000)
def judge_task(submission_id, problem_id):
    uid = Submission.objects.get(id=submission_id).user_id
    JudgeDispatcher(submission_id, problem_id).judge()


@dramatiq.actor
def my_task(arg1, arg2):
    print(f"Processing task with {arg1} and {arg2}")
    sleep(5)
    print(f"Task with {arg1} and {arg2} completed")