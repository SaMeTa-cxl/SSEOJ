import unittest

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import User


class UserLoginTests(TestCase):
    def setUp(self):
        # 注意用户模型创建实体时要使用create_user,否则密码以明文形式存储，authenticate函数无法使用
        user = User.objects.create_user(username='1', email='abc@qq.com', password='123456')
        print("create user")
        print(user.username, user.password, user.email)

    def test_login_success(self):
        data = {'email': 'abc@qq.com', 'password': '123456'}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data['data'], "登录成功")
        self.assertEqual(response.data['err'], None)

    def test_login_fail(self):
        data = {'email': 'abc@qq.com', "password": "123"}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg'], "用户名或密码错误！")
        self.assertEqual(response.data['err'], "error")

    def test_login_with_invalid_field(self):
        data = {'email': 'abc@qq.com'}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'err': 'invalid-password', 'msg': 'password: This field is required.'})
