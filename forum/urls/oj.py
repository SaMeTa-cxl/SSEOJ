from django.urls import path

from ..views.oj import *

urlpatterns = [
    path('post/list/', PostListAPI.as_view(), name='post_list'),
    path('post/<int:post_id>/information/', PostInformationAPI.as_view(), name='post_information'),
    path('post/<int:post_id>/comments/', PostCommentInformationAPI.as_view(), name='post_comments'),
    path('post/comment/new/', PostCommentNewAPI.as_view(), name='post_comment_new'),
    path('post/new/', PostNewAPI.as_view(), name='post_new'),
    path('post/good/', PostGoodAPI.as_view(), name='post_good'),
    path('post/delete/', PostDeleteAPI.as_view(), name='post_delete'),
    path('post/comment/good/', PostCommentGoodAPI.as_view(), name ='post_comment_good'),
    path('post/hot_post/', PostHotAPI.as_view(), name='post_hot_post'),
    path('post/my_post/', PostMyAPI.as_view(), name='post_my_post'),
    path('post/subscribe_post/', PostSubscribeAPI.as_view(), name='post_subscribe_post'),
    path('post/<int:post_id>/comments/<int:comment_id>/', PostSecondaryCommentInformationAPI.as_view(), name='post_subscribe_post'),
]