from django.urls import path

from account.views.oj import UserLoginAPI

urlpatterns = [
    path("login/", UserLoginAPI.as_view(), name="login"),
]