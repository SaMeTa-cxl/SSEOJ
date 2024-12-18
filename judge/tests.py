from django.test import TestCase

from conf.conf import SysConfigs


class JudgeTestCase(TestCase):
    def test_judge(self):
        print(SysConfigs.judge_server_token)
