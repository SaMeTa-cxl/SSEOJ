from django.urls import path

from ..views.oj import *

urlpatterns = [
    path("problem/<int:problem_id>/description/", ProblemDescriptionAPI.as_view(), name="problem_description"),
    path("problem/<int:problem_id>/solutions/", ProblemSolutionsAPI.as_view(), name="problem_solutions"),
    path("solution/good/", SolutionGoodAPI.as_view(), name="solutions_good"),
    path("solution/comment/good/", SolutionCommentGoodAPI.as_view(), name="solutions_comment_good"),
    # path("problem/solutions/<int:solution_id>/comments", SolutionCommentsAPI.as_view(), name="solutions_comment"),
    path("problem/solutions/<int:solution_id>/comments/", SolutionLevel1CommentAPI.as_view(), name="solution_comments1"),
    path("problem/solutions/<int:solution_id>/comments/<int:comment_id>/", SolutionLevel2CommentAPI.as_view(), name="solution_comments2"),
    path("problem/solutions/comment/new/", SolutionCommentNewAPI.as_view(), name="solution_comment_new"),

    path("problem/<int:problem_id>/solutions/<int:solution_id>/",
         ProblemSolutionsDetailAPI.as_view(), name="problem_solutions_detail"),
    path("problem/create/", ProblemCreateAPI.as_view(), name="problem_create"),
    path("problem/star/", ProblemStarAPI.as_view(), name="problem_star"),
    path("solution/create/", ProblemSolutionCreateAPI.as_view(), name="problem_solutions_create"),
    path("problemlist/", ProblemListAPI.as_view(), name="problem_list"),
    path("problemlist/create/", ProblemListCreateAPI.as_view(), name="problem_list_create"),
    path("problemlist/transfer/", ProblemListTransferAPI.as_view(), name="problem_list_transfer"),
    path("problemlist/<int:problemlist_id>/", ProblemListDetailAPI.as_view(), name="problem_list_detail"),
    path("problemlist/star/", ProblemListStarAPI.as_view(), name="problem_list_star"),
    path("problemlist/add_problem/", ProblemListAddProblemAPI.as_view(), name="problem_list_add_problem"),
    path("problemset/", ProblemsetAPI.as_view(), name="problemset"),
    path("study_plan/add/", StudyPlanAddAPI.as_view(), name="study_plan_add_problem"),
    path("study_plan/delete/", StudyPlanDelAPI.as_view(), name="study_plan_del_problem"),
    path("tags/", TagAPI.as_view(), name="tags"),
    path("problemset/problem_num/", ProblemNumWithDifficultyAPI.as_view(), name="tags"),
]