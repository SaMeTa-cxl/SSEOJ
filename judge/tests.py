from django.test import TestCase

from conf.conf import SysConfigs
from judge.dispatcher import process_pending_task


class JudgeTestCase(TestCase):
    def test_judge(self):
        # print(SysConfigs.languages)
        print(list(filter(lambda item: "C++" == item["name"], SysConfigs.languages))[0])
        # process_pending_task()
