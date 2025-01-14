
from django.urls import path

from conf.views import JudgeServerHeartbeatAPI, UploadImageAPI

urlpatterns = [
    path("judge_server_heartbeat/", JudgeServerHeartbeatAPI.as_view(), name="judge_server_heartbeat_api"),
    path("upload/", UploadImageAPI.as_view(), name="upload_image_api"),
]