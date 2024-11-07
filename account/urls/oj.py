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
    path("user/profile_change/", UserProfileChange.as_view(), name="user_profile_change"),
    path("user/name_change/", UserNameChange.as_view(), name="user_name_change"),
    path("user/avatar_change/", UserAvatarChange.as_view(), name="user_avatar_change"),
    path("user/password_change/", UserPasswordChange.as_view(), name="user_profile_change"),
]