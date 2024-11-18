from rest_framework.views import APIView

from forum.models import Post, PostComment
from utils.api import *
from account.models import User


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
    def post(self, request, post_id):
        comment_content = request.data.get('comment_content')
        user_id = request.data.get('user_id')
        reply_to_user_id = request.data.get('reply_to_user_id', None)
        create_time = request.data.get('create_time', None)

        if not post_id or not comment_content or not user_id:
            return fail("评论出问题啦！")

        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        reply_to_user = None
        if reply_to_user_id:
            reply_to_user = User.objects.get(id=reply_to_user_id)

        comment = PostComment.objects.create(
            post=post,
            create_user=user,
            content=comment_content,
            reply_to_user=reply_to_user,
            create_time=create_time
        )

        post.comment_count += 1
        post.save()

        output_data = {"comment_id": comment.id}
        return success(output_data)


class PostNew(APIView):
    def post(self, request):
        post_id = request.POST.get("post_id")
        user_id = request.data.get('user_id')
        post_content = request.POST.get("post_content")
        create_time = request.POST.get("create_time", None)
        tags = request.POST.get("tags", None)

        user = User.objects.get(id=user_id)

        post = Post.objects.create(
            title = "为什么API设计的请求参数中没有title这个字段",
            content = post_content,
            create_user = user,
            create_time = create_time,
        )

        output_data = {"post_id": post.id}
        return success(output_data)



class PostGood(APIView):
    def put(self, request, post_id):
        pass
