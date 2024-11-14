import unittest

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import User, Following


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

    def test_login_with_invalid_field1(self):
        data = {'email': 'abc@qq.com'}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'err': 'invalid-password', 'msg': 'password: This field is required.'})

    def test_login_with_invalid_field2(self):
        data = {'password': '123456'}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'err': 'invalid-email', 'msg': 'email: This field is required.'})

    def test_logout_success(self):
        response = self.client.get(reverse('identity_logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'err': None, 'data': '登出成功'})

    def test_register_success(self):
        data = {'email': 'def@qq.com', 'username': 'user1', 'password': '123456'}
        response = self.client.post(reverse('identity_register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'err': None, 'data': '注册成功！'})

    def test_register_fail1(self):
        data = {'email': 'def@qq.com', 'password': '123456'}
        response = self.client.post(reverse('identity_register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'err': 'error', 'msg': '所有字段均为必填项'})

    def test_register_fail2(self):
        data = {'email': 'abc@qq.com', 'username': 'user1', 'password': '123456'}
        response = self.client.post(reverse('identity_register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'err': 'error', 'msg': '该邮箱已注册'})

class UserSubscribeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='1', email='abc@qq.com', password='password')
    def test_subscribe_success(self):
        self.client.login(email='abc@qq.com', password='password')
        following_user = User.objects.create_user(username='1', email='def@qq.com', password='password')
        in_data = {'user_id': following_user.id, 'relationship': 1}
        response = self.client.post(reverse('user_subscribe'), data=in_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data['data'], "关注成功")
        self.assertEqual(response.data['err'], None)
        self.assertTrue(Following.objects.filter(follower=self.user, following=following_user).exists())

