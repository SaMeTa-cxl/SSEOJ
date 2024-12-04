from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from account.models import User
from .models import Post, PostComment

class ForumTests(TestCase):
    def setUp(self):
        PostComment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
        self.user1 = User.objects.create_user(id=1, username='1', email='abc@qq.com', password='123456')
        self.user2 = User.objects.create_user(id=2, username='2', email='def@qq.com', password='123456')

        self.login_url = reverse('identity_login')
        self.logout_url = reverse('identity_logout')
        self.post_new_url = reverse('post_new')
        self.post_list_url = reverse('post_list')
        self.post_comments_new_url = reverse('post_comment_new')
        self.post_good_url = reverse('post_good')
        self.post_delete_url = reverse('post_delete')

    def post_new(self):
        data = {'email': 'abc@qq.com', 'password': '123456'}
        login_response = self.client.post(reverse('identity_login'), data)

        post_data = {
            'id': 1,
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

    # def test_post_new(self):
    #     response = self.post_new()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('post_id', response.data['data'])
    #     self.assertEqual(Post.objects.count(), 1)
    #     post = Post.objects.first()
    #     self.assertEqual(post.content, '这是一条新帖子内容')
    #     self.assertEqual(post.create_user, self.user1)
    #     self.assertEqual(post.title, 'Title')
    #
    # def test_post_information(self):
    #     Post_new_response = self.post_new()
    #     response = self.client.get(reverse('post_information', kwargs={'post_id': 1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     post = Post.objects.filter(id=1).first()
    #     self.assertEqual(response.data['data']["post_title"], post.title)
    #     self.assertEqual(response.data['data']["like_count"], post.like_count)
    #     self.assertEqual(response.data['data']["comment_count"], post.comment_count)
    #     self.assertEqual(response.data['data']["post_content"], post.content)
    #     self.assertEqual(response.data['data']["create_time"], post.create_time)
    #     self.assertEqual(response.data['data']["user_name"], post.create_user.username)
    #
    #
    #
    # def test_comment_new(self):
    #     post_new_response = self.post_new()
    #     login_user2_response = self.switch_user()
    #     self.assertEqual(login_user2_response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(login_user2_response.data['data'], "登录成功")
    #     self.assertEqual(login_user2_response.data['err'], None)
    #
    #     comment_data = {
    #         'comment_id': 1,
    #         'post_id': 1,
    #         'user_id': self.user2.id,
    #         'comment_content': '这是一条评论',
    #     }
    #     comment_new_reponse = self.client.post(self.post_comments_new_url, comment_data)
    #     self.assertEqual(comment_new_reponse.status_code, status.HTTP_200_OK)
    #     self.assertIn('comment_id', comment_new_reponse.data['data'])
    #     self.assertEqual(PostComment.objects.count(), 1)
    #     comment = PostComment.objects.first()
    #     self.assertEqual(comment.content, '这是一条评论')
    #     self.assertEqual(comment.create_user, self.user2)
    #
    # def test_post_good(self):
    #     post_new_response = self.post_new()
    #     login_user2_response = self.switch_user()
    #     post_good_data = {
    #         'post_id': 1,
    #         'is_good': 1,
    #     }
    #     post_good_response = self.client.put(self.post_good_url, post_good_data, content_type='application/json', format='json')
    #     print(post_good_response.data)
    #     self.assertEqual(post_good_response.status_code, status.HTTP_200_OK)
    #     post = Post.objects.first()
    #     self.assertEqual(post.like_count, 1)
    #
    # def test_delete_post(self):
    #     post_new_response = self.post_new()
    #     data = {'post_id': 1}
    #     response = self.client.delete(reverse('post_delete'), data, content_type='application/json', format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Post.objects.all().count(), 0)

    def test_comment_list(self):
        post_new_response = self.post_new()
        login_user2_response = self.switch_user()
        for i in range(20):
            comment_data = {
                'comment_id': i+1,
                'post_id': 1,
                'user_id': self.user2.id,
                'comment_content': f"Comment {i+1}",
            }
            print(comment_data)
            comment_new_reponse = self.client.post(self.post_comments_new_url, comment_data)
            # self.assertEqual(comment_new_reponse.status_code, status.HTTP_200_OK)
            # self.assertIn('comment_id', comment_new_reponse.data['data'])
            # self.assertEqual(PostComment.objects.count(), i+1)
            # comment = PostComment.objects.filter(id=i+1).first()
            # self.assertEqual(comment.content, f"Comment {i+1}")
            # self.assertEqual(comment.create_user, self.user2)

        self.assertEqual(PostComment.objects.all().count(), 20)
        data = {
            'page_num': 2,
            'page_size': 10,
        }
        response = self.client.get(reverse('post_comments', kwargs={'post_id': 1}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

