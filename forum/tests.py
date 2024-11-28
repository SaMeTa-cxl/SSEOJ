from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from account.models import User
from .models import Post, PostComment

class ForumTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='1', email='abc@qq.com', password='123456')
        self.user2 = User.objects.create_user(username='2', email='def@qq.com', password='123456')

        self.login_url = reverse('identity_login')
        self.logout_url = reverse('identity_logout')
        self.post_new_url = reverse('post_new')
        self.post_list_url = reverse('post_list')
        self.post_comments_new_url = reverse('post_comment_new')
        self.post_good_url = reverse('post_good')
        self.post_delete_url = reverse('post_delete')
        # reverse('post_information', kwargs={'post_id': 1})
        # reverse('post_comments', kwargs={'post_id': 1})


    def post_new(self):
        data = {'email': 'abc@qq.com', 'password': '123456'}
        login_response = self.client.post(reverse('identity_login'), data)

        post_data = {
            'user_id': self.user1.id,
            'post_content': '这是一条新帖子内容',
            'post_title': 'Title',
            'tags': '技术, Django'
        }

        # 发送 POST 请求创建新帖子
        return self.client.post(self.post_new_url, post_data, format='json')

    def switch_user(self):
        logout_response = self.client.get(reverse('identity_logout'))
        self.assertEqual(logout_response.data['data'], "登出成功")
        data = {'email': 'def@qq.com', 'password': '123456'}
        return self.client.post(reverse('identity_login'), data)

    def test_postnew(self):
        response = self.post_new()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('post_id', response.data['data'])
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.content, '这是一条新帖子内容')
        self.assertEqual(post.create_user, self.user1)
        self.assertEqual(post.title, 'Title')

    def test_post_comment_list(self):
        post_new_response = self.post_new()
        login_user2_response = self.switch_user()
        self.assertEqual(login_user2_response.status_code, status.HTTP_200_OK)
        self.assertEqual(login_user2_response.data['data'], "登录成功")
        self.assertEqual(login_user2_response.data['err'], None)

        comment_data = {
            'post_id': 1,
            'user_id': self.user2.id,
            'comment_content': '这是一条评论',
        }
        comment_new_reponse = self.client.post(self.post_comments_new_url, comment_data)
        self.assertEqual(comment_new_reponse.status_code, status.HTTP_200_OK)
        self.assertIn('comment_id', comment_new_reponse.data['data'])
        self.assertEqual(PostComment.objects.count(), 1)
        comment = PostComment.objects.first()
        self.assertEqual(comment.content, '这是一条评论')
        self.assertEqual(comment.create_user, self.user2)

    def test_post_good(self):
        post_new_response = self.post_new()
        login_user2_response = self.switch_user()

        post_good_data = {
            'post_id': 1,
            'is_good': True,
        }
        post_good_response = self.client.put(reverse('post_good'), post_good_data)

        self.assertEqual(post_good_response.status_code, status.HTTP_200_OK)
        post = Post.objects.first()
        self.assertEqual(post.like_count, 1)

