from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from account.models import User

class ForumTests(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='1', email='abc@qq.com', password='123456')
        user2 = User.objects.create_user(username='2', email='cde@qq.com', password='123456')

    def PostnewTest(self):
        data = {'email': 'abc@qq.com', 'password': '123456'}
        response = self.client.post(reverse('identity_login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data['data'], "登录成功")
        self.assertEqual(response.data['err'], None)