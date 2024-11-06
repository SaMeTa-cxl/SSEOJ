from django.urls import path

from account.views.oj import UserLoginApi

urlpatterns = [
    path("login/", UserLoginApi.as_view(), name="login"),
]