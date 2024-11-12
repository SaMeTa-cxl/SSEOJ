import uuid

from django.db import models
from django.db.models import Count

from account.models import User


class TagType(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tag_type'


class Tag(models.Model):
    name = models.CharField(max_length=10)
    type = models.ForeignKey(TagType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # 题目描述
    description = models.TextField()
    # 输入格式
    input_style = models.TextField()
    # 输出格式
    output_style = models.TextField()
    # 提示
    hint = models.TextField(null=True)
    """
    样例
    格式：{
        'input': ["1 2", "3 4" ...],
        'output': ["3", "7", ...]
    }
    """
    sample = models.JSONField()
    tags = models.ManyToManyField(Tag)
    # 取值为1~4的整数，表示从易到难
    difficulty = models.IntegerField()
    # ms
    time_limit = models.IntegerField()
    # KB
    memory_limit = models.IntegerField()
    pass_cnt = models.IntegerField(default=0)
    attempt_cnt = models.IntegerField(default=0)
    source = models.TextField(null=True, blank=True)
    star_cnt = models.IntegerField(default=0)
    star_users = models.ManyToManyField(User, related_name='star_problems')
    pass_users = models.ManyToManyField(User, related_name='pass_problems')
    create_time = models.DateTimeField(auto_now_add=True)
    check_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'problem'
        ordering = ('create_time',)

    def get_pass_status(self, user):
        if user.is_authenticated:
            return self.pass_users.contains(user)
        else:
            return None

    def get_star_status(self, user):
        if user.is_authenticated:
            return self.star_users.contains(user)
        else:
            return None

    def get_similar_problems(self, user):
        similar_problems = (
            Problem.objects
            .exclude(id=self.id)
            .filter(tags__in=self.tags.all())
            .annotate(similarity=Count('tags'))
            .order_by('-similarity')[:4]
        )

        similar_problems = list(similar_problems.values())
        needed_fields = ['id', 'name', 'difficulty', 'pass_status', ]
        for i, problem in enumerate(similar_problems):
            problem['pass_status'] = user in Problem.objects.get(id=problem['id']).pass_users.all()
            similar_problems[i] = {key: problem[key] for key in needed_fields}
        return similar_problems


class ProblemList(models.Model):
    title = models.CharField(max_length=20)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_problem_lists')
    star_users = models.ManyToManyField(User, related_name='star_problem_lists')
    star_count = models.IntegerField(default=0)
    problem_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(null=True)
    summary = models.TextField(blank=True)
    difficulty = models.IntegerField(default=1)
    problems = models.ManyToManyField(Problem, related_name='problem_lists')

    def calculate_difficulty(self):
        """
        计算题单整体难度，使用简单的计算平均数然后四舍五入的方法，返回一个1~4的整数作为难度
        """
        pass

    class Meta:
        db_table = 'problem_list'
        ordering = ('create_time', )


class Solution(models.Model):
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag)
    check_status = models.BooleanField(default=False)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_solutions')
    like_users = models.ManyToManyField(User, related_name='like_solutions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions')

    class Meta:
        db_table = 'solution'
        ordering = ('create_time', )


class SolutionComment(models.Model):
    content = models.TextField()
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solution_comments')
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='comments')
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(User, related_name='like_solution_comments')
    create_time = models.DateTimeField(auto_now_add=True)
    check_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'solution_comment'
        ordering = ('create_time', )


class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_plan')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='study_plan')
    added_time = models.DateTimeField(auto_now_add=True)
    problem_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'study_plan'
