import hashlib
import json
from urllib.parse import urljoin

import requests
from django.core.cache import cache
from django.db import transaction
from django.db.models import F

from account.models import User
from conf.conf import SysConfigs
from judge.models import JudgeServer
from problem.models import Problem
from submission.models import Submission, JudgeStatus
from utils.constants import CacheKey


def process_pending_task():
    tmp = cache.get(CacheKey.waiting_queue, [])
    tmp = []
    if len(tmp):
        # 防止循环引入
        from judge.tasks import judge_task
        tmp_data = tmp.pop(-1)
        cache.set(CacheKey.waiting_queue, tmp)
        if tmp_data:
            data = json.loads(tmp_data.decode("utf-8"))
            judge_task.send(**data)


class ChooseJudgeServer:
    def __init__(self):
        self.server = None

    def __enter__(self) -> [JudgeServer, None]:
        with transaction.atomic():
            # 选择最轻松的cpu核来判题
            servers = JudgeServer.objects.select_for_update().filter(is_disabled=False).order_by("task_number")
            servers = [s for s in servers if s.status == "normal"]
            for server in servers:
                if server.task_number <= server.cpu_core * 2:
                    server.task_number = F("task_number") + 1
                    server.save(update_fields=["task_number"])
                    self.server = server
                    return server
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            JudgeServer.objects.filter(id=self.server.id).update(task_number=F("task_number") - 1)


class DispatcherBase(object):
    def __init__(self):
        self.token = hashlib.sha256(SysConfigs.judge_server_token.encode("utf-8")).hexdigest()

    def _request(self, url, data=None):
        kwargs = {"headers": {"X-Judge-Server-Token": self.token}}
        if data:
            kwargs["json"] = data
        return requests.post(url, **kwargs).json()


class JudgeDispatcher(DispatcherBase):
    def __init__(self, submission_id, problem_id):
        super().__init__()
        self.submission = Submission.objects.get(id=submission_id)
        self.last_result = self.submission.result if self.submission.info else None
        self.problem = Problem.objects.get(id=problem_id)

    def _compute_statistic_info(self, resp_data):
        # 用时和内存占用保存为多个测试点中最长的那个
        self.submission.statistic_info["time_cost"] = max([x["cpu_time"] for x in resp_data])
        self.submission.statistic_info["memory_cost"] = max([x["memory"] for x in resp_data])

        # sum up the score in OI mode
        # if self.problem.rule_type == ProblemRuleType.OI:
        #     score = 0
        #     try:
        #         for i in range(len(resp_data)):
        #             if resp_data[i]["result"] == JudgeStatus.ACCEPTED:
        #                 resp_data[i]["score"] = self.problem.test_case_score[i]["score"]
        #                 score += resp_data[i]["score"]
        #             else:
        #                 resp_data[i]["score"] = 0
        #     except IndexError:
        #         logger.error(f"Index Error raised when summing up the score in problem {self.problem.id}")
        #         self.submission.statistic_info["score"] = 0
        #         return
        #     self.submission.statistic_info["score"] = score

    def judge(self):
        language = self.submission.language
        sub_config = list(filter(lambda item: language == item["name"], SysConfigs.languages))[0]

        code = self.submission.code

        data = {
            "language_config": sub_config["config"],
            "src": code,
            "max_cpu_time": self.problem.time_limit,
            "max_memory": 1024 * 1024 * self.problem.memory_limit,
            "test_case_id": self.problem.test_case_id,
            "output": True,
        }

        with ChooseJudgeServer() as server:
            if not server:
                data = {"submission_id": self.submission.id, "problem_id": self.problem.id}
                tmp = cache.get(CacheKey.waiting_queue, [])
                cache.set(CacheKey.waiting_queue, tmp.append(data))
                return
            Submission.objects.filter(id=self.submission.id).update(result=JudgeStatus.JUDGING)
            resp = self._request(urljoin(server.service_url, "/judge"), data=data)

        if not resp:
            Submission.objects.filter(id=self.submission.id).update(result=JudgeStatus.SYSTEM_ERROR)
            return

        if resp["err"]:
            self.submission.result = JudgeStatus.COMPILE_ERROR
            self.submission.statistic_info["err_info"] = resp["data"]
            self.submission.statistic_info["score"] = 0
        else:
            resp["data"].sort(key=lambda x: int(x["test_case"]))
            self.submission.info = resp
            self._compute_statistic_info(resp["data"])
            error_test_case = list(filter(lambda case: case["result"] != JudgeStatus.ACCEPTED, resp["data"]))

            # 取第一个错误的测试用例的错误类型为该次提交的评测结果
            if not error_test_case:
                self.submission.result = JudgeStatus.ACCEPTED
            else:
                self.submission.result = error_test_case[0]["result"]
        self.submission.save()
        self.update_problem_status()
        # 判题结束，尝试处理任务队列中剩余的任务
        process_pending_task()

    def update_problem_status(self):
        result = str(self.submission.result)
        problem_id = str(self.problem.id)
        with transaction.atomic():
            # update problem status
            problem = Problem.objects.select_for_update().get(id=self.problem.id)
            problem.attempt_cnt += 1
            if self.submission.result == JudgeStatus.ACCEPTED and self.last_result != JudgeStatus.ACCEPTED:
                problem.pass_cnt += 1
                problem.pass_users.add(User.objects.get(id=self.submission.user_id))
            problem.save(update_fields=["attempt_cnt", "pass_cnt", "pass_users"])

            score = self.submission.statistic_info["score"]
