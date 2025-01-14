from datetime import timezone

from rest_framework.views import APIView
from django.db.models import Q, F
from forum.models import Post, PostComment
from forum.serializers import PostCommentSerializer
from utils.api import *
from account.models import User
from problem.models import Tag

class PostListAPI(APIView):
    def get(self, request):
        sort_type = request.GET.get('sort_type', 'likeDesc')
        key_word = request.GET.get('keyword', None)
        print(key_word)

        if sort_type == 'timeAsc':
            postData = Post.objects.filter(
                Q(is_announcement=False) &
                Q(check_status=True) &
                (Q(title__icontains=key_word) if key_word else Q())
            ).order_by('create_time')
        elif sort_type == 'timeDesc':
            postData = Post.objects.filter(
                Q(is_announcement=False) &
                Q(check_status=True) &
                (Q(title__icontains=key_word) if key_word else Q())
            ).order_by('-create_time')
        else:
            postData = Post.objects.filter(
                Q(is_announcement=False) &
                Q(check_status=True) &
                (Q(title__icontains=key_word) if key_word else Q())
            ).order_by('-like_count')

        count = postData.count()
        postData = paginate_data(request, postData)
        postList = []

        for post in postData:
            # print(post.title)
            postRelateData = {}
            creatUser = post.create_user

            postRelateData['post_id'] = post.id
            postRelateData['post_title'] = post.title
            postRelateData['id'] = creatUser.id
            postRelateData['username'] = creatUser.username
            postRelateData['avatar'] = ImageCode.image_base64(creatUser.avatar)
            postRelateData['like_count'] = post.like_count
            postRelateData['comment_count'] = post.comment_count
            postRelateData['create_time'] = post.create_time

            postList.append(postRelateData)

        return success({'count': count, 'post_list': postList})

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
            "name": post.create_user.username,
            "id": post.id,
            "avatar": ImageCode.image_base64(post.create_user.avatar),
        }

        return success(post_data)

class PostCommentInformationAPI(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return fail("要找的帖子走丢啦！")

        self_id = request.user.id
        comments = PostComment.objects.filter(Q(post_id=post_id) & Q(check_status=True)& Q(under_comment_id__isnull=True))
        count = comments.count()
        comments = paginate_data(request, comments)

        serializer = PostCommentSerializer(comments, many=True, context={'request': request})
        # 返回数据
        comment_data = {
            "count": count,
            "comments": serializer.data
        }
        return success(comment_data)


class PostSecondaryCommentInformationAPI(APIView):
    def get(self, request, post_id, comment_id):
        if not Post.objects.filter(id=post_id).exists():
            return fail("要找的帖子走丢啦！")
        if not PostComment.objects.filter(id=comment_id).exists():
            return fail("这条评论走丢啦！")

        print(request.data)

        comments = PostComment.objects.filter(Q(post_id=post_id) & Q(check_status=True)& Q(under_comment_id=comment_id))
        count = comments.count()
        comments = paginate_data(request, comments)

        serializer = PostCommentSerializer(comments, many=True, context={'request': request})
        # 返回数据
        comment_data = {
            "count": count,
            "comments": serializer.data
        }
        return success(comment_data)


class PostCommentNewAPI(APIView):
    def post(self, request):
        """
        if not request.user.is_authenticated:
            return fail('未登录！')
        post_id = request.data.get('post_id')
        comment_id = request.data.get('comment_id')
        comment_content = request.data.get('comment_content')
        user_id = request.user.id
        reply_to_user_id = request.data.get('reply_to_user_id', None)
        under_comment_id = request.data.get('under_comment_id', None)

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
                    under_comment_id=under_comment_id,
                )
            else:
                comment = PostComment.objects.create(
                    id=comment_id,
                    post=post,
                    create_user=user,
                    content=comment_content,
                    reply_to_user=reply_to_user,
                    under_comment_id=under_comment_id,
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
        """
        if not request.user.is_authenticated:
            return fail(msg = '未登录')

        post_id = request.data.get('id', None)
        reply_to_id = request.data.get('reply_to_id', None)
        under_comment_id = request.data.get('under_comment_id', None)
        if post_id is None:
            return fail('帖子不存在')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return fail('帖子不存在')

        comment = PostComment.objects.create(post = post, create_user = request.user, content = request.data.get('content'),
    reply_to_user_id = reply_to_id,
    under_comment_id_id = under_comment_id)
        comment.save()

        return success('评论成功')


class PostNewAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("未登录！")
        post_id = request.POST.get("id")
        user_id = request.user.id
        post_content = request.data.get("post_content")
        post_title = request.data.get("post_title", None)
        tags = request.data.get("tags", [])


        user = User.objects.get(id=user_id)

        if not post_id:
            post = Post.objects.create(
                title = post_title,
                content = post_content,
                create_user = user,
            )
        else:
            post = Post.objects.create(
                id=post_id,
                title=post_title,
                content=post_content,
                create_user=user,
            )

        for tagId in tags:
            try:
                tag = Tag.objects.get(id=tagId)
            except Tag.DoesNotExist:
                continue

            post.tags.add(tag)


        output_data = {"post_id": post.id}
        return success(output_data)

class PostGoodAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("未登录！")
        user_id = request.user.id
        post_id = request.data.get('post_id')
        is_good = request.data.get('is_good')
        print("userid", user_id)
        print("postid", post_id)
        print(is_good)

        try:
            post = Post.objects.get(id=post_id)
            user = User.objects.get(id=user_id)
        except (Post.DoesNotExist, User.DoesNotExist):
            print("exception")
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

class PostCommentGoodAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail(msg = '未登录')

        data = request.data
        user = request.user
        try:
            userId = int(data.get('id', 'error'))
            isGood = bool(data.get('is_good', 'error'))
        except ValueError:
            return fail(msg = '未知的数据类型')

        try:
            comment = PostComment.objects.get(id = userId)
        except PostComment.DoesNotExist:
            return fail(msg = '没有找到该评论')

        if isGood:
            comment.like_users.add(user)
            comment.like_count = F('like_count') + 1
        else:

            comment.like_users.remove(user)
            comment.like_count = F('like_count') - 1
        comment.save()

        return success('操作成功')


class PostHotAPI(APIView):
    def get(self, request):
        page_num = int(request.GET.get('page_num', 1))
        page_size = int(request.GET.get('page_size', 30))
        #print(page_num, page_size)
        postData = Post.objects.order_by('-like_count')[(page_num - 1) * page_size: page_num * page_size]
        postList = []

        for post in postData:
            #print(post.title)
            postRelateData = {}
            creatUser = post.create_user

            postRelateData['post_id'] = post.id
            postRelateData['post_title'] = post.title
            postRelateData['id'] = creatUser.id
            postRelateData['username'] = creatUser.username
            postRelateData['avatar'] = ImageCode.image_base64(creatUser.avatar)
            postRelateData['like_count'] = post.like_count
            postRelateData['comment_count'] = post.comment_count
            postRelateData['create_time'] = post.create_time

            postList.append(postRelateData)
        has_next = page_num * page_size < Post.objects.count()
        return success({'posts': postList, 'has_next': has_next})


class PostMyAPI(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return success({'posts': [], 'has_next': False})

        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 30)
        postData = Post.objects.filter(create_user=request.user)
        has_next = page_num * page_size < postData.count()
        postData = postData[(page_num - 1) * page_size: page_num * page_size]
        postList = []

        for post in postData:
            postRelateData = {}
            creatUser = post.create_user

            postRelateData['post_id'] = post.id
            postRelateData['post_title'] = post.title
            postRelateData['id'] = creatUser.id
            postRelateData['username'] = creatUser.username
            postRelateData['avatar'] = ImageCode.image_base64(creatUser.avatar)
            postRelateData['like_count'] = post.like_count
            postRelateData['comment_count'] = post.comment_count
            postRelateData['create_time'] = post.create_time

            postList.append(postRelateData)
        return success({'posts': postList, 'has_next':has_next})


class PostSubscribeAPI(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return success({'posts': [], 'has_next': False})

        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 30)
        postData = Post.objects.filter(create_user__in=request.user.followings.all())
        has_next = page_num * page_size < postData.count()
        postData = postData[(page_num - 1) * page_size: page_num * page_size]
        postList = []

        for post in postData:
            postRelateData = {}
            creatUser = post.create_user

            postRelateData['post_id'] = post.id
            postRelateData['post_title'] = post.title
            postRelateData['id'] = creatUser.id
            postRelateData['username'] = creatUser.username
            postRelateData['avatar'] = ImageCode.image_base64(creatUser.avatar)
            postRelateData['like_count'] = post.like_count
            postRelateData['comment_count'] = post.comment_count
            postRelateData['create_time'] = post.create_time

            postList.append(postRelateData)
        return success({'posts': postList, 'has_next': has_next})
