import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserType(object):
    NORMAL_USER = 'Normal'
    ADMIN = 'Admin'


class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True, default="")
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.TextField(null=True, blank=True)
    avatar = models.CharField(max_length=50, default='static/avatar.png/')
    # 用户类型：Normal/Admin
    user_type = models.CharField(max_length=20, default=UserType.NORMAL_USER)
    # 我的关注
    following = models.ManyToManyField('self', related_name='follower', symmetrical=False, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
