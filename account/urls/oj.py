from django.urls import path

from account.views.oj import *


urlpatterns = [
    path("identity/login/", UserLoginAPI.as_view(), name="identity_login"),
    path("identity/logout/", UserLogoutAPI.as_view(), name="identity_logout"),
    path("identity/send_email/", UserSendEmail.as_view(), name="identity_send_email"),
    path("identity/register/", UserRegister.as_view(), name="identity_register"),
    path("user/info/", UserInfo.as_view(), name="user_info"),
    path("user/subscribe/", UserSubscribe.as_view(), name="user_subscribe"),
    path("user/{int: user_id}/following/", UserFollowing.as_view(), name="user_following"),
    path("user/{int: user_id}/follower/", UserFollower.as_view(), name="user_follower"),
    path("user/info_change/", UserInfoChange.as_view(), name="user_info_change")
]