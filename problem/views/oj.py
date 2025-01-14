import pickle

from django.db.models import Q, F, ExpressionWrapper, FloatField
from rest_framework.views import APIView

from account.models import User
from problem.models import Problem, Solution, ProblemList, Tag, SolutionComment
from problem.serializers import ProblemSerializer, SolutionSerializer, ProblemListSerializer, \
    ProblemListDetailSerializer, SolutionCreateSerializer, TagSerializer, ProblemListCreateSerializer, \
    ProblemCreateSerializer, SolutionCommentSerializer
from utils.api import success, fail, paginate_data, validate_serializer, ImageCode

sort_dict = {
    'likeDesc': '-like_count',
    'commentDesc': '-comment_count',
    'timeDesc': '-create_time',
    'timeAsc': 'create_time',
    'idAsc': 'id',
    'idDesc': '-id',
    'countAsc': 'problem_count',
    'countDesc': '-problem_count',
    'starAsc': 'star_count',
    'starDesc': '-star_count',
    'diffAsc': 'difficulty',
    'diffDesc': '-difficulty',
}


class ProblemDescriptionAPI(APIView):
    @staticmethod
    def get(request, problem_id):
        """
        获取id为problem_id的题目的详细信息，包括题目的所有字段信息和请求用户的pass_status和star_status
        注：当用户未登录时，pass_status、star_status均为None
        """
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        serializer = ProblemSerializer(problem)
        response_data = serializer.data
        response_data['similar_problems'] = problem.get_similar_problems(request.user)
        response_data['pass_status'] = problem.get_pass_status(request.user)
        response_data['star_status'] = problem.get_star_status(request.user)
        # print(response_data)
        return success(response_data)


class ProblemSolutionsAPI(APIView):

    @staticmethod
    def get(request, problem_id):
        """
        获取id为problem_id的题目的所有题解信息，其中详细内容被截断为最多200个字符
        返回为一个字典列表，每个字典为一个题解的信息
        """
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        solutions = problem.solutions.all()
        keyword = request.GET.get('keyword')
        tags = request.GET.get('tags')
        sort_type = request.GET.get('sort_type')
        if keyword:
            solutions = solutions.filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
        if tags:
            solutions = solutions.filter(tags__in=tags)
        if sort_type:
            solutions = solutions.order_by(sort_dict[sort_type])
        else:
            solutions = solutions.order_by('-create_time')
        solutions = paginate_data(request, solutions, SolutionSerializer)
        taglist = set()
        for i in range(len(solutions)):
            solutions[i]['content'] = solutions[i]['content'][:200]
            solutions[i]['user_info']['avatar'] = ImageCode.image_base64(solutions[i]['user_info']['avatar'])
            taglist = taglist.union(set(solutions[i]['tags']))
        return success({'count': len(solutions), 'solutions': solutions, 'taglist': list(taglist)})


class ProblemSolutionsDetailAPI(APIView):
    @staticmethod
    def get(request, problem_id, solution_id):
        """
        返回题解的详细信息，完整的solution_content
        """
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return fail('该题目不存在！')
        try:
            solution = problem.solutions.get(id=solution_id)
        except Solution.DoesNotExist:
            return fail('该题解不存在')

        # 获取是否点赞
        rsp = SolutionSerializer(solution).data
        rsp['is_like'] = solution.is_like(request.user)

        return success(rsp)


class ProblemListAPI(APIView):
    def get(self, request):
        """
        根据标题或简介中的关键字筛选未删除的、公开的、非请求用户自己的题单列表；如果用户未登录，则获取所有含有关键字的公开未删除题单，且题单的
        每道题目中的pass_count字段为null；
        如果关键字为空，则返回所有未删除的、公开的、非请求用户的题单；
        """
        keyword = request.GET.get('keyword', '')
        problem_lists = ProblemList.objects.filter((Q(title__icontains=keyword) | Q(summary__icontains=keyword))
                                                   & Q(is_deleted=False) & Q(is_public=True))

        sort_type = request.GET.get('sort_type', 'idAsc')
        problem_lists = problem_lists.order_by(sort_dict[sort_type])

        if not request.user.is_authenticated:
            response_data = paginate_data(request, problem_lists, ProblemListSerializer)
            for problem_list in response_data:
                problem_list['pass_count'] = None
                problem_list['is_star'] = False
            return success({'count': problem_lists.count(), 'problemlists': response_data})

        response_data = paginate_data(request, problem_lists, ProblemListSerializer)
        # response_data为list,problem_list为字典
        for problem_list in response_data:
            problem_list_entity = ProblemList.objects.get(id=problem_list['id'])
            problem_list['is_star'] = problem_list_entity.star_users.contains(request.user)
            problem_list['pass_count'] = 0
            # problem_list['id']取自于数据库，可保证存在，不需要处理异常
            for problem in problem_list_entity.problems.all():
                if problem.get_pass_status(request.user):
                    problem_list['pass_count'] += 1

        return success({'count': problem_lists.count(), 'problemlists': response_data})


class ProblemListCreateAPI(APIView):
    @validate_serializer(ProblemListCreateSerializer)
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        title = request.data['title']
        summary = request.data['summary']
        is_public = request.data['type']
        ProblemList.objects.create(title=title, summary=summary, is_public=is_public, create_user=request.user)
        return success('创建成功')


class ProblemListTransferAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        to_transfer_list = ProblemList.objects.get(id=request.data['id'])
        ProblemList.objects.create(tittle=to_transfer_list.title,
                                   summary=to_transfer_list.summary,
                                   create_user=request.user,
                                   problem_count=to_transfer_list.problem_count,
                                   problems=to_transfer_list.problems,
                                   )
        return success('转存成功！')


class ProblemListDetailAPI(APIView):
    def get(self, request, problemlist_id):
        """
        获取id为problemlist_id的题单的详细信息。
        用户未登录时或题单id不存在时，返回对应的错误信息
        """
        try:
            problem_list = ProblemList.objects.get(id=problemlist_id)
        except ProblemList.DoesNotExist:
            return fail("该题单不存在！")

        response_data = ProblemListDetailSerializer(problem_list).data
        if request.user.is_authenticated:
            response_data['star_status'] = problem_list.get_star_status(request.user)
        else:
            response_data['star_status'] = None

        problems = response_data['problems']
        response_data['pass_count'] = 0
        for problem in problems:
            problem['pass_status'] = Problem.objects.get(id=problem['id']).get_pass_status(request.user)
            if problem['pass_status']: response_data['pass_count'] += 1

        return success(response_data)

    def put(self, request, problemlist_id):
        """
        向题单添加或删除题目，路径中有一个problemlist_id参数
        另外需要传递name、summary、add、delete,
        add和delete分别为要添加或删除的题目id列表
        problem_ids表示需要操作的题目id列表，is_add表示操作为添加或删除的题目id列表
        为空时表示不修改
        当用户未登录或题单创建者不是请求用户或题单不存在时返回相应的错误
        当添加的题目已经存在题单或删除的题目不在题单之中，返回相应的错误
        """
        add = request.data['add']
        delete = request.data['delete']
        name = request.data['name']
        summary = request.data['summary']
        add_problems = Problem.objects.filter(id__in=add)
        del_problems = Problem.objects.filter(id__in=delete)
        try:
            problem_list = ProblemList.objects.get(id=problemlist_id)
        except ProblemList.DoesNotExist:
            return fail("该题单不存在！")
        if not request.user.is_authenticated or problem_list.create_user != request.user:
            return fail('用户无权限！')

        if add:
            if problem_list.problems.filter(id__in=add).count() == len(add):
                return fail('添加的题目已经存在于题单之中！')
            problems_in_list = problem_list.problems.filter(id__in=add)
            problem_list.add_problem(add_problems.difference(problems_in_list))

        if problem_list.problems.filter(id__in=delete).count() != 0:
            problems_in_list = problem_list.problems.filter(id__in=delete)
            problem_list.remove_problem(problems_in_list)
        else:
            return fail('删除的题目不在题单之中')

        if name:
            problem_list.title = name
        if summary:
            problem_list.summary = summary
        problem_list.save()

    def delete(self, request, problemlist_id):
        """
        删除一个题单，如果题单收藏数为0，直接删除记录，否则软删除，只是将is_deleted字段设为true，使其不会被get出来，当收藏数为0时再硬删除
        当题单不存在或用户未登录或请求用户非创建者时返回相应的错误
        """
        try:
            problem_list = ProblemList.objects.get(id=problemlist_id)
        except ProblemList.DoesNotExist:
            return fail('该题单不存在！')
        if not request.user.is_authenticated or problem_list.create_user != request.user:
            return fail('用户无权限！')

        if problem_list.star_users.exists():
            problem_list.is_deleted = True
            problem_list.save()
        else:
            problem_list.delete()
        return success("删除成功")


class ProblemListStarAPI(APIView):
    def post(self, request):
        """
        收藏/取消收藏一个题单
        用户未登录或题单不存在时返回相应错误
        当被取消收藏的题单收藏数为0且已经被发布者删除时硬删除此题单
        """
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        try:
            problem_list = ProblemList.objects.get(id=request.data['problemlist_id'])
        except ProblemList.DoesNotExist:
            return fail('不存在该题单！')
        if int(request.data['is_star']) == 0:
            if not problem_list.star_users.contains(request.user):
                return fail('你并未收藏该题单噢~')
            problem_list.star_users.remove(request.user)
            problem_list.remove_star_count()
            if not problem_list.star_users.exists() and problem_list.is_deleted:
                problem_list.delete()
            return success('取消收藏！')
        else:
            if problem_list.star_users.contains(request.user):
                return fail('你已经收藏了该题单噢~')
            problem_list.star_users.add(request.user)
            problem_list.add_star_count()
            return success('收藏成功！')


class ProblemListAddProblemAPI(APIView):
    def post(self, request):
        try:
            problem_list = ProblemList.objects.get(id=request.data['problemlist_id'])
        except ProblemList.DoesNotExist:
            return fail('题单不存在！')

        try:
            problem = Problem.objects.get(id=request.data['problem_id'])
        except Problem.DoesNotExist:
            return fail('题目不存在')

        problem_list.add_problem(problem)


class ProblemSolutionCreateAPI(APIView):
    @validate_serializer(SolutionCreateSerializer)
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("用户未登录！")
        try:
            problem = Problem.objects.get(id=request.data['problem_id'])
        except Problem.DoesNotExist:
            return fail("不存在该题目！")
        tags = Tag.objects.filter(id__in=request.data.get('tags', []))
        solution = Solution.objects.create(content=request.data['content'], problem=problem,
                                           create_user=request.user, title=request.data['title'])
        solution.tags.set(tags)
        solution.save()
        return success('创建成功')


class TagAPI(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return success(serializer.data)


class ProblemsetAPI(APIView):
    def get(self, request):
        """
        获取题库，根据keyword、min_difficulty、max_difficulty、tags进行筛选，根据sort_type进行排序
        可选的sort_type: idAsc（默认） || idDesc || diffAsc || diffDesc || passRateAsc || passRateDesc
        返回所有的题目信息
        """
        keyword = request.GET.get('keyword', '')
        min_difficulty = request.GET.get('min_difficulty')
        max_difficulty = request.GET.get('max_difficulty')
        tags = request.GET.getlist('tags[]')
        sort_type = request.GET.get('sort_type', 'idAsc')

        problems = Problem.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
        if min_difficulty:
            problems = problems.filter(difficulty__gte=min_difficulty)
        if max_difficulty:
            problems = problems.filter(difficulty__lte=max_difficulty)
        if tags:
            problems = problems.filter(tags__in=tags)
        if sort_type[:8] == 'passRate':
            problems = problems.annotate(
                            pass_rate=ExpressionWrapper(
                                F('passed_count') / F('attempt_count'),
                                output_field=FloatField()
                            )
                        ).order_by('pass_rate' if sort_type == 'passRateAsc' else '-pass_rate')
        else:
            problems = problems.order_by(sort_dict[sort_type])
        problems = paginate_data(request, problems, ProblemSerializer)
        for problem in problems:
            if request.user.is_authenticated:
                problem['pass_status'] = Problem.objects.get(id=problem['id']).get_pass_status(request.user)
            else:
                problem['pass_status'] = None

        resp = {"count": len(problems), 'problems': problems}
        return success(resp)


class ProblemCreateAPI(APIView):
    @validate_serializer(ProblemCreateSerializer)
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        tags = request.data.pop('tags')
        samples = request.data.pop('samples')
        request.data['sample'] = samples
        problem = Problem.objects.create(**request.data)
        if tags:
            problem.tags.set(Tag.objects.filter(id__in=tags))
        return success('创建成功')


class ProblemStarAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        try:
            problem = Problem.objects.get(id=request.data['id'])
        except Problem.DoesNotExist:
            return fail('题目不存在！')

        if request.data['relationship']:
            problem.star_users.add(request.user)
        else:
            problem.star_users.remove(request.user)


class StudyPlanAddAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        id = request.GET.get['id']
        if not id:
            return fail('请传入题目id')
        request.user.study_plan.add(Problem.objects.get(id=request.data['id']))


class StudyPlanDelAPI(APIView):
    def delete(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        id = request.GET.get['id']
        if not id:
            return fail('请传入题目id')
        request.user.study_plan.add(Problem.objects.get(id=request.GET.get['id']))


class SolutionGoodAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("用户未登录！")
        try:
            solution = Solution.objects.get(id=request.data['id'])
        except Solution.DoesNotExist:
            return fail('该题解不存在！')

        if request.data['is_good']:
            solution.like_users.add(request.user)
            solution.like_count = F('like_count') + 1
            solution.save()
        else:
            solution.like_users.remove(request.user)
            solution.like_count = F('like_count') - 1
            solution.save()


class SolutionCommentGoodAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail("用户未登录！")
        try:
            comment = SolutionComment.objects.get(id=request.data['id'])
        except SolutionComment.DoesNotExist:
            return fail('该题解不存在！')

        if request.data['is_good']:
            comment.like_users.add(request.user)
            comment.like_count = F('like_count') + 1
            comment.save()
        else:
            comment.like_users.remove(request.user)
            comment.like_count = F('like_count') - 1
            comment.save()


class SolutionCommentsAPI(APIView):
    def get(self, request):
        try:
            solution = Solution.objects.get(id=request.data['id'])
        except Solution.DoesNotExist:
            return fail('该题解不存在！')

        comments = solution.comments.all()
        comments = paginate_data(request, comments, SolutionCommentSerializer)

        for comment in comments:
            comment['is_good'] = SolutionComment.objects.get(id=comment['id']).like_users.contains(request.user)

        return success({'count': len(comments), 'comments': comments})

class SolutionLevel1CommentAPI(APIView):
    def get(self, request, solution_id):
        try:
            solution = Solution.objects.get(id=solution_id)
        except Solution.DoesNotExist:
            return fail('该题解不存在！')

        comments = solution.comments.filter(under_comment__isnull = True)
        comments_num = comments.count()
        comments = paginate_data(request, comments, SolutionCommentSerializer)

        comments_data = []

        for comment in comments:
            comment_tmp = {}
            comment_tmp['id'] = comment['id']
            user_info_tmp = {}
            user_info_tmp['id'] = comment['user_info']['id']
            user_info_tmp['username'] = comment['user_info']['username']
            user_info_tmp['avatar'] = ImageCode.image_base64(comment['user_info']['avatar'])
            comment_tmp['user_info'] = user_info_tmp
            if not request.user.is_authenticated:
                comment_tmp['is_good'] = False
            else:
                comment_tmp['is_good'] = SolutionComment.objects.get(id=comment['id']).like_users.contains(request.user)
            comment_tmp['content'] = comment['content']
            comment_tmp['like_count'] = comment['like_count']
            comment_tmp['create_time'] = comment['create_time']
            under_comments = SolutionComment.objects.get(id=comment['id']).under_comment
            if under_comments is not None:
                comment_tmp['comments_count'] = under_comments.count()
            else:
                comment_tmp['comments_count'] = 0
            comments_data.append(comment_tmp)

        return success({'count': comments_num, 'comments': comments_data})

class SolutionLevel2CommentAPI(APIView):
    def get(self, request, solution_id, comment_id):
        """
        try:
            solution = Solution.objects.get(id=solution_id)
        except Solution.DoesNotExist:
            return fail('该题解不存在！')

        comments = solution.comments.filter(under_comment=comment_id)
        comments = paginate_data(request, comments, SolutionCommentSerializer)

        comments_data = []

        for comment in comments:
            comment_tmp = {}
            comment_tmp['id'] = comment['id']
            user_info_tmp = {}
            user_info_tmp['id'] = comment['create_user']['id']
            user_info_tmp['username'] = comment['create_user']['username']
            user_info_tmp['avatar'] = ImageCode.image_base64(comment['create_user']['avatar'])
            comment_tmp['user_info'] = user_info_tmp
            if not request.user.is_authenticated:
                comment_tmp['is_good'] = False
            else:
                comment_tmp['is_good'] = SolutionComment.objects.get(id=comment['id']).like_users.contains(request.user)
            comment_tmp['content'] = comment['content']
            comment_tmp['like_count'] = comment['like_count']
            comment_tmp['create_time'] = comment['create_time']
            comment_tmp['reply_to_id'] = comment['reply_to_user'].id
            comment_tmp['reply_to_name'] = SolutionComment.objects.get(id=comment['id']).reply_to_user.username
            comments_data.append(comment_tmp)
        """

        try:
            comment = SolutionComment.objects.get(id=comment_id)
        except SolutionComment.DoesNotExist:
            return fail(msg = '一级评论不存在')
        level2_comments = comment.under_comments.all()
        level2_comments_num = level2_comments.count()
        level2_comments = paginate_data(request, level2_comments, SolutionCommentSerializer)

        comments_data = []

        for level2_comment in level2_comments:
            comment_tmp = {}
            comment_tmp['id'] = level2_comment['id']
            user_info_tmp = {}
            user_info_tmp['id'] = level2_comment['create_user']['id']
            user_info_tmp['username'] = level2_comment['create_user']['username']
            user_info_tmp['avatar'] = ImageCode.image_base64(level2_comment['create_user']['avatar'])
            comment_tmp['user_info'] = user_info_tmp
            if not request.user.is_authenticated:
                comment_tmp['is_good'] = False
            else:
                comment_tmp['is_good'] = comment.like_users.contains(request.user)
            comment_tmp['content'] = level2_comment['content']
            comment_tmp['like_count'] = level2_comment['like_count']
            comment_tmp['create_time'] = level2_comment['create_time']
            comment_tmp['reply_to_id'] = level2_comment['reply_to_user_info']['id']
            comment_tmp['reply_to_name'] = level2_comment['reply_to_user_info']['username']
            comments_data.append(comment_tmp)

        return success({'count': level2_comments_num, 'comments': comments_data})

class SolutionCommentNewAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return fail('用户未登录！')
        try:
            solution = Solution.objects.get(id=request.data['id'])
        except Solution.DoesNotExist:
            return fail('该题解不存在！')

        content = request.data['content']
        reply_to_id = request.data.get('reply_to_id', None)
        under_comment_id = request.data.get('under_comment_id', None)
        reply_to_user = None
        comment = None
        if reply_to_id is not None:
            try:
                reply_to_user = User.objects.get(id=reply_to_id)
            except User.DoesNotExist:
                return fail(msg = '回复用户不存在')
        if under_comment_id is not None:
            try:
                comment = SolutionComment.objects.get(id=under_comment_id)
            except SolutionComment.DoesNotExist:
                return fail(msg = '回复的评论不存在')

        if comment is None:
            SolutionComment.objects.create(content = content, create_user = request.user, solution = solution)
        else:
            if reply_to_user is None:
                SolutionComment.objects.create(content = content, create_user = request.user, solution = solution, under_comment = comment)
            else:
                SolutionComment.objects.create(content=content, create_user=request.user, solution=solution,
                                               reply_to_user=reply_to_user, under_comment=comment)

        return success("评论成功")


class ProblemNumWithDifficultyAPI(APIView):
    def get(self, request):
        rsp = []
        for i in range(1, 7):
            rsp.append(Problem.objects.filter(difficulty=i).count())
        return success(rsp)
