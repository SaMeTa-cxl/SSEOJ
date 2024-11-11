from django.urls import path

from ..views.oj import *

urlpatterns = [
    path("problem/<int:problem_id>/description/", ProblemDescriptionAPI.as_view(), name="problem_description"),
    path("problem/<int:problem_id>/solutions/", ProblemSolutionsAPI.as_view(), name="problem_solutions"),
    path("problem/<int:problem_id>/solutions/<int:solution_id>/",
         ProblemSolutionsDetailAPI.as_view(), name="problem_solutions_detail"),
    path("problem/<int:problem_id>/submissions/", ProblemSubmissionsAPI.as_view(), name="problem_submissions"),
    path("problem/submit/", ProblemSubmitAPI.as_view(), name="problem_submit"),
    path("solution/create/", ProblemSolutionCreateAPI.as_view(), name="problem_solutions_create"),
    path("problemlist/", ProblemListAPI.as_view(), name="problem_list"),
    path("problemlist/<int:problemlist_id>/", ProblemListDetailAPI.as_view(), name="problem_list_detail"),
    path("problemlist/star/", ProblemListStarAPI.as_view(), name="problem_list_star"),
    path("problemset/", ProblemsetAPI.as_view(), name="problemset"),
]