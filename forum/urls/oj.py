from django.urls import path

from ..views.oj import *

urlpatterns = [
    path('post/list/', PostListAPI.as_view(), name='post_list'),
    path('post/<int:post_id>/information/', PostInformationAPI.as_view(), name='post_information'),
    path('post/<int:post_id>/comments/', PostCommentInformationAPI.as_view(), name='post_comments'),
    path('post/comment/new/', PostCommentNewAPI.as_view(), name='post_comment_new'),
    path('post/new/', PostNewAPI.as_view(), name='post_new'),
    path('post/good/', PostGoodAPI.as_view(), name='post_good'),
    path('post/delete/', PostDeleteAPI.as_view(), name='post_delete')
]