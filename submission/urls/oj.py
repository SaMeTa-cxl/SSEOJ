from django.urls import path

from ..views.oj import *

urlpatterns = [
    path("problem/submit/", ProblemSubmitAPI.as_view(), name="problem_submit"),
    path("problem/<int:problem_id>/submissions/", ProblemSubmissionsAPI.as_view(), name="problem_submissions")
]