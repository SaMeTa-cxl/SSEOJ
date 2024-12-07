from datetime import timezone

from rest_framework.views import APIView
from django.db.models import Q
from forum.models import Post, PostComment
from utils.api import *
from account.models import User

class PostListAPI(APIView):
    def get(self, request):
        self_id = request.user.id
        count = Post.objects.all().count()
        posts = Post.objects.all()
        posts = paginate_data(request, posts)
        post_array = []
        post_data = {}

        for post in posts:
            tmp = {}
            tmp['post_id'] = post.id
            tmp['post_title'] = post.title
            tmp['user_id'] = post.create_user.id
            tmp['username'] = post.create_user.username
            tmp['avatar'] = post.create_user.avatar
            tmp['like_count'] = post.like_users.count()
            tmp['comment_count'] = PostComment.objects.filter(post=post).count()
            post_array.append(tmp)

        post_data["count"] = count
        post_data["posts"] = post_array

        return success(post_data)

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
            "post_content": post.content,
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
        count = PostComment.objects.filter(Q(post_id=post_id) & Q(check_status=True)).count()
        comments = PostComment.objects.filter(Q(post_id=post_id) & Q(check_status=True))
        comments = paginate_data(request, comments)
        comment_array = []
        comment_data = {}

        for comment in comments:
            tmp = {}
            tmp['comment_id'] = comment.id
            tmp['user_id'] = comment.create_user.id
            tmp['user_name'] = comment.create_user.username
            tmp['avatar'] = comment.create_user.avatar
            tmp['like_status'] = comment.like_users.filter(id=self_id).exists()
            tmp['comment_content'] = comment.content
            tmp['like_count'] = comment.like_count
            tmp['create_time'] = comment.create_time
            tmp['reply_to_id'] = comment.reply_to_user.id if comment.reply_to_user else None
            tmp['reply_to_name'] = comment.reply_to_user.username if comment.reply_to_user else None
            comment_array.append(tmp)

        comment_data["count"] = count
        comment_data["comments"] = comment_array

        return success(comment_data)

class PostCommentNewAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('未登录！')
        post_id = request.data.get('post_id')
        comment_id = request.data.get('comment_id')
        comment_content = request.data.get('comment_content')
        user_id = request.user.id
        reply_to_user_id = request.data.get('reply_to_user_id', None)

        if not post_id or not comment_content or not user_id:
            return fail("评论出问题啦！")

        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        if reply_to_user_id:
            reply_to_user = User.objects.get(id=reply_to_user_id)
            if not comment_id:
                comment = PostComment.objects.create(
                    post=post,
                    create_user=user,
                    content=comment_content,
                    reply_to_user=reply_to_user,
                )
            else:
                comment = PostComment.objects.create(
                    id=comment_id,
                    post=post,
                    create_user=user,
                    content=comment_content,
                    reply_to_user=reply_to_user,
                )
        else:
            if not comment_id:
                comment = PostComment.objects.create(
                    post=post,
                    create_user=user,
                    content=comment_content,
                )
            else:
                comment = PostComment.objects.create(
                    id=comment_id,
                    post=post,
                    create_user=user,
                    content=comment_content,
                )

        post.comment_count += 1
        post.save()

        output_data = {"comment_id": comment.id}
        return success(output_data)


class PostNewAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("未登录！")
        post_id = request.POST.get("id")
        user_id = request.user.id
        post_content = request.POST.get("post_content")
        post_title = request.POST.get("post_title", None)
        tags = request.POST.get("tags", None)

        user = User.objects.get(id=user_id)

        if not post_id:
            post = Post.objects.create(
                title = post_title,
                content = post_content,
                create_user = user,
                tags = tags
            )
        else:
            post = Post.objects.create(
                id=post_id,
                title=post_title,
                content=post_content,
                create_user=user,
                tags=tags
            )

        output_data = {"post_id": post.id}
        return success(output_data)


class PostGoodAPI(APIView):
    def put(self, request):
        if not request.user.is_authenticated:
            return fail("未登录！")
        user_id = request.user.id
        post_id = request.data.get('post_id')
        is_good = request.data.get('is_good')
        print("userid", user_id)
        print("postid", post_id)

        try:
            post = Post.objects.get(id=post_id)
            user = User.objects.get(id=user_id)
        except (Post.DoesNotExist, User.DoesNotExist):
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
        if not request.user.is_authenticated:
            return fail("未登录")
        post_id = request.data.get('post_id')
        if not post_id:
            return fail("缺少post_id参数")

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return fail("帖子不存在！")

        if(post.create_user != request.user):
            return fail("无权限删除该帖子") #理论上不会出现，因为对于无权限的用户前端不会显示删除功能

        post.delete()
        return success("帖子成功删除！")
