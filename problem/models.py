import uuid

from django.db import models


class ProblemTag(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'problem_tag'


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
    tags = models.ManyToManyField(ProblemTag)
    difficulty = models.IntegerField()
    # ms
    time_limit = models.IntegerField()
    # KB
    memory_limit = models.IntegerField()
    pass_cnt = models.IntegerField(default=0)
    attempt_cnt = models.IntegerField(default=0)
    source = models.TextField(null=True, blank=True)
    star_cnt = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    check_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'problem'
        ordering = ('create_time',)
