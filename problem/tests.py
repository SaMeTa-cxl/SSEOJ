import copy

from django.test import TestCase
from django.urls import reverse

from account.models import User
from problem.models import Problem, Tag, Solution, ProblemList

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
    """
    测试ProblemDescriptionAPI
    """
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
        problem2.tags.add(self.tag1)
        problem3 = Problem.objects.create(**{**DEFAULT_PROBLEM_DATA, 'name': "Test Problem 3"})
        problem3.tags.add(self.tag2, self.tag1)
        problem3.pass_users.add(self.user)

        self.login()
        self.get_description()
        print(self.data)
        # 测试状态码
        self.assertEqual(self.response.status_code, 200)
        # 测试业务逻辑无误
        self.assertEqual(self.response.data['err'], None)

        # 测试样例无误
        sample = self.data['sample']
        self.assertEqual(sample['input'], ["1 2", "2 3"])
        # 测试tags无误
        tags = self.data['tags']
        self.assertEqual(tags, [self.tag1.name, self.tag2.name])

        # 测试similar_problem
        similar_problems = self.data['similar_problems']
        self.assertEqual(len(similar_problems), 2)
        self.assertEqual(similar_problems[0]['id'], problem3.id)
        self.assertEqual(similar_problems[1]['id'], problem2.id)
        self.assertEqual(similar_problems[0]['pass_status'], True)
        self.assertEqual(similar_problems[1]['pass_status'], False)

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

    def test_problem_get_fail(self):
        """
        测试访问不存在的题目
        """
        data = self.client.get(reverse('problem_description', args=[100])).data
        self.assertEqual(data['msg'], '该题目不存在！')


class SolutionTestCase(TestCase):
    def setUp(self):
        self.problem = Problem.objects.create(**DEFAULT_PROBLEM_DATA)
        self.user = User.objects.create_user(username="test", email="123@qq.com", password="123456")
        self.solution1 = Solution.objects.create(title="title", content="content1", problem=self.problem, create_user=self.user)
        self.solution2 = Solution.objects.create(title="title", content="content2", problem=self.problem, create_user=self.user)

    def tearDown(self):
        Problem.objects.all().delete()
        User.objects.all().delete()
        Solution.objects.all().delete()

    def test_problem_get_fail(self):
        # 测试题目获取失败
        self.client.login(email="123@qq.com", password="123456")
        msg = self.client.get(reverse("problem_solutions", args=[100])).data['msg']
        self.assertEqual(msg, '该题目不存在！')

    def test_user_unauthorized(self):
        # 测试用户未登录
        msg = self.client.get(reverse("problem_solutions", args=[self.problem.id])).data['msg']
        self.assertEqual(msg, '用户未登录')

    def test_success(self):
        # 测试正常成功获取
        self.client.login(email="123@qq.com", password="123456")
        data = self.client.get(reverse("problem_solutions", args=[self.problem.id])).data['data']
        print(data)
        solution = data['solutions']
        needed_fields = ['id', 'username', 'avatar']
        for field in needed_fields:
            self.assertIsNotNone(data[0]['user_info'][field])
        self.assertEqual(len(data), 2)
        self.assertEqual(self.solution1.id, data[0]['id'])
        self.assertEqual(self.solution1.content, data[0]['content'])

        # 测试题解信息截断
        self.solution1.content = "content1" * 100
        self.solution1.save()
        data = self.client.get(reverse("problem_solutions", args=[self.problem.id])).data['data']
        self.assertEqual(len(data[0]['content']), 200)

    def test_full_content(self):
        # 测试完整的题解内容
        self.solution1.content = "content1" * 100
        self.solution1.save()
        data = self.client.get(reverse("problem_solutions_detail", args=[self.problem.id, self.solution1.id])).data['data']
        self.assertEqual(len(data), 800)


class ProblemListTestCase(TestCase):
    """
    测试请求题单列表的api
    """
    def setUp(self):
        self.problem = Problem.objects.create(**DEFAULT_PROBLEM_DATA)
        self.user = User.objects.create_user(username="username", email="123@qq.com", password="123")
        another_user = User.objects.create_user(username="another", email='321@qq.com', password="123")
        self.problem_list = ProblemList.objects.create(title='title', create_user=another_user, is_public=True)
        self.problem_list.add_problem(Problem.objects.filter(id=self.problem.id))

    def tearDown(self):
        ProblemList.objects.all().delete()
        Problem.objects.all().delete()
        User.objects.all().delete()

    def test_success(self):
        request_data = {'keyword': '', 'page_num': 1, 'page_size': 10}
        data = self.client.get(reverse("problem_list"), request_data).data['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], self.problem_list.title)
        self.assertIsNone(data[0]['pass_count'])
        self.assertEqual(self.problem_list.difficulty, 1)

        self.client.login(email="123@qq.com", password="123")
        self.problem.pass_users.add(self.user)
        data = self.client.get(reverse("problem_list"), request_data).data['data']
        self.assertEqual(data[0]['pass_count'], 1)


class ProblemListDetailTestCase(TestCase):
    """
    测试获取题单详细信息，题单添加或删除题目，删除题单api
    """
    def setUp(self):
        self.user = User.objects.create_user(username="username", email="123@qq.com", password="123")
        self.problem_list = ProblemList.objects.create(title='title', create_user=self.user, is_public=True)

    def tearDown(self):
        ProblemList.objects.all().delete()
        Problem.objects.all().delete()
        User.objects.all().delete()

    def test_user_unauthorized(self):
        msg = self.client.get(reverse("problem_list_detail", args=[self.problem_list.id])).data['msg']
        self.assertEqual(msg, "用户未登录！")

    def test_problem_list_nonexistent(self):
        self.client.login(email="123@qq.com", password="123")
        msg = self.client.get(reverse("problem_list_detail", args=[100])).data['msg']
        self.assertEqual(msg, "该题单不存在！")

    def test_get_success(self):
        self.client.login(email="123@qq.com", password="123")
        data = self.client.get(reverse("problem_list_detail", args=[self.problem_list.id])).data['data']
        print(data)

    def test_put_success(self):
        self.assertEqual(self.problem_list.problems.count(), 0)
        self.assertEqual(self.problem_list.problem_count, 0)
        self.assertEqual(self.problem_list.difficulty, 0)

        self.client.login(email="123@qq.com", password="123")
        p1 = Problem.objects.create(**DEFAULT_PROBLEM_DATA)
        p2 = Problem.objects.create(**{**DEFAULT_PROBLEM_DATA, 'name': "Test Problem 2", "difficulty": 4})
        p3 = Problem.objects.create(**{**DEFAULT_PROBLEM_DATA, 'name': "Test Problem 3"})
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p1.id, p2.id], 'is_add': True},
                               content_type="application/json").data['data']
        # 测试部分添加题目存在于题单中的情况
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p2.id, p3.id], 'is_add': True},
                               content_type="application/json").data['data']
        self.assertEqual(data, "添加成功")
        self.problem_list.refresh_from_db()
        self.assertEqual(self.problem_list.difficulty, 2)
        self.assertEqual(self.problem_list.problems.count(), 3)
        self.assertEqual(self.problem_list.problem_count, 3)
        # 测试全部添加题目都在题单中的情况
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p2.id, p3.id], 'is_add': True},
                               content_type="application/json").data['msg']
        self.assertEqual(data, "添加的题目已经存在于题单之中！")
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p1.id], 'is_add': False},
                               content_type="application/json").data['data']
        # 测试部分删除题目不存在于题单中的情况
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p1.id, p3.id], 'is_add': False},
                               content_type="application/json").data['data']
        self.assertEqual(data, "删除成功")
        self.problem_list.refresh_from_db()
        self.assertEqual(self.problem_list.difficulty, 4)
        self.assertEqual(self.problem_list.problems.count(), 1)
        self.assertEqual(self.problem_list.problem_count, 1)
        # 测试所有删除题目都不存在于提单中的情况
        data = self.client.put(reverse("problem_list_detail", args=[self.problem_list.id]),
                               data={'problem_ids': [p1.id, p3.id], 'is_add': False},
                               content_type="application/json").data['msg']
        self.assertEqual(data, "删除的题目不在题单之中")

    def test_delete_success(self):
        self.client.login(email="123@qq.com", password="123")
        self.client.post(reverse("problem_list_star"), data={"problemlist_id": self.problem_list.id})
        # 软删除
        data = self.client.delete(reverse("problem_list_detail", args=[self.problem_list.id])).data['data']
        self.assertEqual(data, '删除成功')
        self.problem_list.refresh_from_db()
        self.assertTrue(self.problem_list.is_deleted)
        self.assertTrue(ProblemList.objects.all().contains(self.problem_list))
        # 收藏数为0时硬删除
        self.client.post(reverse("problem_list_star"), data={"problemlist_id": self.problem_list.id})
        self.assertFalse(ProblemList.objects.all().contains(self.problem_list))
        # 在ProblemListStarAPI中被硬删除
        self.problem_list = ProblemList.objects.create(title='title', create_user=self.user, is_public=True)
        self.client.delete(reverse("problem_list_detail", args=[self.problem_list.id]))
        self.assertFalse(ProblemList.objects.all().contains(self.problem_list))


class ProblemListStarTestCase(TestCase):
    def setUp(self):
        self.problem = Problem.objects.create(**DEFAULT_PROBLEM_DATA)
        self.user = User.objects.create_user(username="username", email="123@qq.com", password="123")
        self.problem_list = ProblemList.objects.create(title='title', create_user=self.user, is_public=True)
        self.problem_list.add_problem(self.problem)

    def tearDown(self):
        ProblemList.objects.all().delete()
        Problem.objects.all().delete()
        User.objects.all().delete()

    def test_success(self):
        self.client.login(email="123@qq.com", password="123")
        data = self.client.post(reverse("problem_list_star"), data={"problemlist_id": self.problem_list.id}).data['data']
        self.assertEqual(data, '收藏成功！')
        self.assertTrue(self.problem_list.star_users.contains(self.user))
        self.problem_list.refresh_from_db()
        self.assertEqual(self.problem_list.star_count, 1)

        data = self.client.post(reverse("problem_list_star"), data={"problemlist_id": self.problem_list.id}).data['data']
        self.assertEqual(data, '取消收藏！')
        self.assertFalse(self.problem_list.star_users.contains(self.user))
        self.problem_list.refresh_from_db()
        self.assertEqual(self.problem_list.star_count, 0)
