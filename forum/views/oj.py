from rest_framework.views import APIView

from forum.models import Post, PostComment
from utils.api import *
from account.models import User

class PostListAPI(APIView):
    def get(self, request):
        pass

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


class PostCommentInformationAPI(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return fail("要找的帖子走丢啦！")

        self_id = request.user.id
        count = PostComment.objects.filter(post_id=post_id).count()
        comments = PostComment.objects.filter(post_id=post_id)
        comments = paginate_data(request, comments)
        comment_array = []
        comment_data = {}

        for comment in comments:
            tmp = {}
            tmp['user_id'] = comment.create_user.id
            tmp['user_name'] = comment.create_user.username
            tmp['avatar'] = comment.create_user.avatar
            tmp['like_status'] = comment.like_users.filter(id=self_id).exists()
            tmp['comment_content'] = comment.content
            tmp['like_count'] = comment.like_count
            tmp['create_time'] = comment.create_time
            tmp['reply_to_id'] = comment.reply_to_user.id
            tmp['reply_to_name'] = comment.reply_to_user.username
            comment_array.append(tmp)

        comment_data["count"] = count
        comment_data["comments"] = comment_array

        return success(comment_data)

class PostCommentNewAPI(APIView):
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


class PostNewAPI(APIView):
    def post(self, request):
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


class PostGoodAPI(APIView):
    def put(self, request, post_id):
        user_id = request.data.get('user_id')
        is_good = request.data.get('is_good')

        try:
            post = Post.objects.get(id=post_id)
            user = User.objects.get(id=user_id)
        except Post.DoesNotExist or User.DoesNotExist:
            return Response({"error": "帖子不存在或用户登录过期！"}, status=404)

        if is_good:
            if user not in post.like_users.all():
                post.like_users.add(user)
                post.like_count += 1
                post.save()
                return success("点赞成功，感谢你的支持！")
        else:
            if user in post.like_users.all():
                post.like_users.remove(user)
                post.like_count -= 1
                post.save()
                return success("取消点赞!")

class PostDeleteAPI(APIView):
    def delete(self, request):
        pass
