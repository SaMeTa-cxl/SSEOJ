from django.urls import path

from ..views.oj import *

urlpatterns = [
    path("problem/<int:problem_id>/description/", ProblemDescriptionAPI.as_view(), name="problem_description"),
    path("problem/<int:problem_id>/solutions/", ProblemSolutionsAPI.as_view(), name="problem_solutions"),
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
]