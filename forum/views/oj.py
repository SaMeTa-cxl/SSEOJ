from rest_framework.views import APIView

from forum.models import Post, PostComment
from utils.api import *


class PostInformationAPI(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return fail("要找的帖子走丢啦！")

        post_data = {
            "post_title": post.title,
            "like_count": post.like_count,
            "comment_count": post.comment_count,
            "post_content": post.post_content,
            "create_time": post.create_time,
            "user_name": post.create_user.username,
        }

        return success(post_data)


class PostCommentInformation(APIView):
    def get(self, request, comment_id):
        try:
            comment = PostComment.objects.get(id=comment_id)
        except PostComment.DoesNotExist:
            return fail("要找的评论走丢啦！")

        comment_data = {
            "post_id": comment.post_id,
            "post_comment_id": comment_id,
            "user_id": comment.create_user.id,
            "comment_content": comment.content,
            "like_count": comment.like_count,
            "create_time": comment.create_time,
            "reply_to_username": comment.reply_to_user.username,
            # "page": comment.page, #这个评论具体在哪一页应该是根据某个函数算出来的吧，前面评论的长度都会影响这条评论所在页数
        }

        return success(comment_data)


class PostCommentNew(APIView):
    def post(self, request, problem_id):
        pass


class PostNew(APIView):
    def post(self, request, problem_id):
        pass


class PostGood(APIView):
    def put(self, request, problem_id):
        pass
