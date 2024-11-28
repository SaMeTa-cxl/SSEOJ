from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from account.models import User
from .models import Post, PostComment

class ForumTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='1', email='abc@qq.com', password='123456')
        self.user2 = User.objects.create_user(username='2', email='cde@qq.com', password='123456')

        self.login_url = reverse('identity_login')
        self.post_new_url = reverse('post_new')
        self.post_list_url = reverse('post_list')
        self.post_comments_new_url = reverse('post_comment_new')
        self.post_good_url = reverse('post_good')
        self.post_delete_url = reverse('post_delete')
        # reverse('post_information', kwargs={'post_id': 1})
        # reverse('post_comments', kwargs={'post_id': 1})

    def test_postnew(self):
        data = {'email': 'abc@qq.com', 'password': '123456'}
        login_response = self.client.post(reverse('identity_login'), data)
        # token = login_response.data.get('token')

        post_data = {
            'user_id': self.user1.id,
            'post_content': '这是一条新帖子内容',
            'post_title': 'Title',
            'tags': '技术, Django'
        }

        # 设置 Authorization header
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        # 发送 POST 请求创建新帖子
        response = self.client.post(self.post_new_url, post_data, format='json')

        # 确保帖子创建成功，返回 200 状态码
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 确保返回的数据中包含 post_id
        self.assertIn('post_id', response.data['data'])

        # 确保数据库中创建了新帖子
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.content, '这是一条新帖子内容')
        self.assertEqual(post.create_user, self.user1)
        self.assertEqual(post.title, 'Title')
        print(post.content)
