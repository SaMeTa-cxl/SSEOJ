from django.urls import path

from account.views.oj import *


urlpatterns = [
    path("identity/login/", UserLoginAPI.as_view(), name="identity_login"),
    path("identity/logout/", UserLogoutAPI.as_view(), name="identity_logout"),
    path("identity/send_email/", UserSendEmailAPI.as_view(), name="identity_send_email"),
    path("identity/register/", UserRegisterAPI.as_view(), name="identity_register"),
    path("user/{int: user_id}/info/", UserInfoAPI.as_view(), name="user_info"),
    path("user/subscribe/", UserSubscribeAPI.as_view(), name="user_subscribe"),
    path("user/{int: user_id}/following/", UserFollowingAPI.as_view(), name="user_following"),
    path("user/{int: user_id}/follower/", UserFollowerAPI.as_view(), name="user_follower"),
    path("user/info_change/", UserInfoChangeAPI.as_view(), name="user_info_change"),
    path("user/{int: user_id}/problemlist/", UserProblemlistAPI.as_view(), name="user_problemlist"),
]