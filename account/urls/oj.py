from django.urls import path

from account.views.oj import *


urlpatterns = [
    path("identity/send_email/", EmailCodeAPI.as_view(), name="api_send_email"),
    path("identity/register/", UserRegisterAPI.as_view(), name="identity_register"),
    path("identity/login/", UserLoginAPI.as_view(), name="identity_login"),
    path("identity/logout/", UserLogoutAPI.as_view(), name="identity_logout"),

    path("user/<int:id>/info/", UserInfoAPI.as_view(), name="user_info"),
    path("user/subscribe/", UserSubscribeAPI.as_view(), name="user_subscribe"),
    path("user/<int:id>/following/", UserFollowingAPI.as_view(), name="user_following"),
    path("user/<int:id>/follower/", UserFollowerAPI.as_view(), name="user_follower"),
    path("user/<int:id>/study_plan/", StudyPlanAPI.as_view(), name="user_study_plan"),
    path("user/profile_change/", UserProfileChangeAPI.as_view(), name="user_profile_change"),
    path("user/user_name_change/", UserNameChangeAPI.as_view(), name="user_name_change"),
    path("user/avatar_change/", UserAvatarChangeAPI.as_view(), name="user_avatar_change"),
    path("user/password_change/", UserPasswordChangeAPI.as_view(), name="user_password_change"),
    path("user/password_forget/", UserPasswordForgetAPI.as_view(), name="user_password_forget"),
    path("user/<int:user_id>/practice/", GetTryProblemAPI.as_view(), name="user_practice"),
    path("user/<int:user_id>/default_problemlist/", StarProblemAPI.as_view(), name="user_default_problemlist"),
    path("user/<int:user_id>/create_problemlist/", UserProblemListAPI.as_view(), name="user_problem_list")
]