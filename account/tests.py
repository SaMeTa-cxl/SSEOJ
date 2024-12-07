import json
import unittest, os, base64
from idlelib.rpc import response_queue

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Following
from utils.api import ImageCode, VerificationCode, DecodePassword
from django.core.cache import cache


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
        self.user = User.objects.create_user(username='1', email='abc@qq.com', password='123')
    def test_subscribe_success(self):
        self.client.login(email='abc@qq.com', password='123')
        # self.client.cookies['user_id'] = self.user.id
        following_user = User.objects.create_user(username='1', email='def@qq.com', password='456')
        in_data = {'id': following_user.id, 'relationship': "1"}
        response = self.client.post(reverse('user_subscribe'), in_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], "关注成功")
        self.assertEqual(response.data['err'], None)
        self.assertTrue(Following.objects.filter(follower=self.user, following=following_user).exists())

class UserInfoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(id=1, username='456', email='1@qq.com', password='123', profile='Nihao')

    def test_getUserInfoTest1(self):
        url = reverse('user_info', kwargs={'user_id': 1})
        response = self.client.get(url)

        # 检查状态码
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查内容
        data = response.data['data']
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['username'], '456')
        self.assertEqual(data['profile'], 'Nihao')
        self.assertEqual(data['subscribing_count'], 0)
        self.assertEqual(data['subscribers_count'], 0)

    def test_getUserInfoTest2(self):
        url = reverse('user_info', kwargs={'user_id': 2})

        response = self.client.get(url)

        print(response.data)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '用户不存在')

class UserInfoChangeTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='1', email='abc@qq.com', password='123', id=1, profile='nihao')
        self.user2 = User.objects.create_user(username='2', email='cba@qq.com', password='456', id=2, profile='wohao')

    def test_profileChange1(self):
        client = APIClient()
        client.force_login(self.user1)
        url = reverse('user_profile_change')
        data = {'user_id': '1', 'profile': 'hello world'}
        response = client.put(url, data)

        data = response.data['data']
        self.user1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, '修改成功')
        self.assertEqual(self.user1.profile, 'hello world')

    def test_profileChange2(self):
        client = APIClient()
        url = reverse('user_profile_change')
        data = {'user_id': '3', 'profile': 'hello world'}
        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '不存在该用户')

    def test_profileChange3(self):
        url = reverse('user_profile_change')
        client = APIClient()
        client.force_login(self.user1)
        data = {'user_id': '2', 'profile': 'hello world'}
        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '没有权限修改')

    def test_userNameChange1(self):
        client = APIClient().force_login(self.user1)
        url = reverse('user_name_change')
        data = {"user_id": '1', 'user_name': '3'}

        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], None)
        self.assertEqual(response.data['data'], '修改成功')

        self.user1.refresh_from_db()
        self.assertEqual(self.user1.username, '3')

    def test_userNameChange2(self):
        client = APIClient()
        client.force_login(self.user1)
        url = reverse('user_name_change')
        data = {"user_id": '2', 'user_name': '3'}

        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '没有权限修改')

    def test_userNameChange3(self):
        client = APIClient()
        url = reverse('user_name_change')
        data = {"user_id": '3', 'user_name': '3'}

        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '不存在该用户')

    def test_userPasswordChange1(self):
        client = APIClient()
        client.force_login(self.user1)
        url = reverse('user_password_change')
        data = {"user_id": '1', 'password': '456'}
        response = self.client.put(url, data)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], None)
        self.assertEqual(response.data['data'], 'success')
        self.assertEqual(self.user.password, '456')

    def test_userPasswordChange2(self):
        url = reverse('user_password_change')
        data = {"user_id": '2', 'password': '465'}

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], 'User not found')

    def test_userAvatarChange1(self):
        client = APIClient()
        client.force_login(self.user)
        url = reverse('user_avatar_change')
        str = ImageCode.image_base64('static/test.png')

        data = {"user_id": '1', 'avatar': str}
        response = client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], None)
        self.assertEqual(response.data['data'], 'success')

        self.user.refresh_from_db()
        self.assertEqual(self.user.avatar, 'static/user_1.png')

    def test_userAvatarChange2(self):
        url = reverse('user_avatar_change')
        str = ImageCode.image_base64('static/test.png')
        data = {"user_id": '2', 'avatar': str}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], 'User not found')

class VerificationCodeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='1', email='3181478797@qq.com', password='123', id=1,
                                             profile='nihao')

    """
    def test_EmailCode1(self):
        client = APIClient()
        data = {"email": "3181478797@qq.com", "type": 0}
        url = reverse('api_send_email')

        response = client.post(url, data)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], None)
        self.assertEqual(response.data['data'], '发送成功')

        print(cache.get("3181478797@qq.com"))

    def test_EmailCode2(self):
        client = APIClient()
        client.force_login(self.user)
        data = {"email": "3181478797@qq.com", "type": 0}
        url = reverse('api_send_email')

        response = client.post(url, data)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '已登录无法获取注册验证码')

    def test_EmailCode3(self):
        client = APIClient()
        client.force_login(self.user)
        url = reverse('api_send_email')

        data = {"email": "abc@qq.com", "type": 0}
        response = self.client.post(url, data)

        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], 'error')
        self.assertEqual(response.data['msg'], '该邮箱已注册')
    """

    def test_EmailCode4(self):
        client = APIClient()
        client.force_login(self.user)
        url = reverse('api_send_email')

        data = {"email": "3181478797@qq.com", "type": 1}
        response = self.client.post(url, data)

        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['err'], None)
        self.assertEqual(response.data['data'], '发送成功')

        print(cache.get("3181478797@qq.com"))

class RegisterTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='1', email='3181478797@qq.com', password='123', id=1,
                                              profile='nihao')

    def test_Resister1(self):
        client = APIClient()
        email = '3181478797@qq.com'
        url = reverse('api_send_email')
        data = {"email": email, "type": 0}
        response = client.post(url, data)

        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['err'], None)
        self.assertEqual(data['data'], "发送成功")

        code = input()

        url = reverse('identity_register')
        data = {"email": '3181478797@qq.com', 'password': '1', 'username': '1', 'verification_code': code}
        response = client.post(url, data)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['err'], None)
        self.assertEqual(data['data'], '注册成功')

        user = User.objects.get(email=email)
        self.assertTrue(user is not None)
        self.assertTrue(user.check_password('1'))
        self.assertEqual(user.username, '1')

        return
