import copy

from django.test import TestCase
from django.urls import reverse

from account.models import User
from problem.models import Problem, TagType, Tag

DEFAULT_PROBLEM_DATA = {
    'name': 'Test Problem 1',
    'description': 'description',
    'input_style': 'input_style',
    'output_style': 'output_style',
    'sample': {
        "input": [
            "1 2",
            "2 3"
        ],
        "output": [
            "3",
            "5"
        ]
    },
    'difficulty': 1,
    'time_limit': 1000,
    'memory_limit': 130000
}


class ProblemDescriptionTestCase(TestCase):
    def setUp(self):
        # 准备好一个题目，设定它的tag
        self.problem = Problem.objects.create(**DEFAULT_PROBLEM_DATA)
        self.tag_type = TagType.objects.create(name='TagType')
        self.tag1 = Tag.objects.create(name='Tag1', type=self.tag_type)
        self.tag2 = Tag.objects.create(name='Tag2', type=self.tag_type)
        self.problem.tags.add(self.tag1, self.tag2)

        # 准备一个用户
        self.user = User.objects.create_user(username='test', email='123@qq.com', password='password')

    def tearDown(self):
        Problem.objects.all().delete()
        Tag.objects.all().delete()
        User.objects.all().delete()
        TagType.objects.all().delete()

    def login(self):
        # 登录用户
        self.client.post(reverse('identity_login'), {'email': '123@qq.com', 'password': 'password'})

    def get_description(self):
        # 发起题目详细信息请求
        self.response = self.client.get(reverse('problem_description', args=[self.problem.id]))
        self.data = self.response.data['data']

    def test_success(self):
        """
        测试正常请求成功的返回结果
        """
        # 添加2个有类似tag的题目
        problem2 = Problem.objects.create(**{**DEFAULT_PROBLEM_DATA, 'name': "Test Problem 2"})
        problem2.tags.add(self.tag1, self.tag2)
        problem3 = Problem.objects.create(**{**DEFAULT_PROBLEM_DATA, 'name': "Test Problem 3"})
        problem3.tags.add(self.tag2)
        problem3.pass_users.add(self.user)

        self.login()
        self.get_description()
        # 测试状态码
        self.assertEqual(self.response.status_code, 200)
        # 测试业务逻辑无误
        self.assertEqual(self.response.data['err'], None)

        # 测试样例无误
        sample = self.data['sample']
        self.assertEqual(sample['input'], ["1 2", "2 3"])
        # 测试tags无误
        tags = self.data['tags']
        self.assertEqual(tags, [self.tag1.id, self.tag2.id])

        # 测试similar_problem

    def test_pass_status(self):
        """
        测试用户登录情况下的通过状态
        """
        self.login()
        self.get_description()
        self.assertEqual(self.data['pass_status'], False)
        # 让该用户通过这个题目
        self.problem.pass_users.add(self.user)
        self.get_description()
        data = self.response.data['data']
        self.assertEqual(data['pass_status'], True)

    def test_star_status(self):
        """
        测试用户登录情况下的收藏状态
        """
        self.login()
        self.get_description()
        self.assertEqual(self.data['star_status'], False)
        # 让该用户收藏这个题目
        self.problem.star_users.add(self.user)
        self.get_description()
        self.assertEqual(self.data['star_status'], True)

    def test_user_unauthorized(self):
        """
        测试用户未登录情况下的请求结果
        """
        self.get_description()

        self.assertEqual(self.data['star_status'], None)
        self.assertEqual(self.data['pass_status'], None)
