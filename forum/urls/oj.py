from django.urls import path

from ..views.oj import *

urlpatterns = [
    path('post/information/', PostInformationAPI.as_view(), name='post_information'),
    path('post/comment/information/', PostCommentInformation.as_view(), name='post_comment_information'),
    path('post/comment/new/', PostCommentNew.as_view(), name='post_comment_new'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/good/', PostGood.as_view(), name='post_good'),
]