
from django.urls import path

from conf.views import JudgeServerHeartbeatAPI

urlpatterns = [
    path("judge_server_heartbeat/", JudgeServerHeartbeatAPI.as_view(), name="judge_server_heartbeat_api"),
]