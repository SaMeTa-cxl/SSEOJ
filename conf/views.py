from django.utils import timezone
from rest_framework.views import APIView
from conf.serializers import JudgeServerHeartbeatSerializer
from judge.models import JudgeServer
from utils.api import validate_serializer, success
from judge.dispatcher import process_pending_task


class JudgeServerHeartbeatAPI(APIView):
    @validate_serializer(JudgeServerHeartbeatSerializer)
    def post(self, request):
        data = request.data

        try:
            server = JudgeServer.objects.get(hostname=data["hostname"])
            server.judger_version = data["judger_version"]
            server.cpu_core = data["cpu_core"]
            server.memory_usage = data["memory"]
            server.cpu_usage = data["cpu"]
            server.service_url = data["service_url"]
            server.ip = request.ip
            server.last_heartbeat = timezone.now()
            server.save(update_fields=["judger_version", "cpu_core", "memory_usage", "service_url", "ip", "last_heartbeat"])
        except JudgeServer.DoesNotExist:
            JudgeServer.objects.create(hostname=data["hostname"],
                                       judger_version=data["judger_version"],
                                       cpu_core=data["cpu_core"],
                                       memory_usage=data["memory"],
                                       cpu_usage=data["cpu"],
                                       ip=request.META["REMOTE_ADDR"],
                                       service_url=data["service_url"],
                                       last_heartbeat=timezone.now(),
                                       )
        # 新server上线 处理队列中的提交，防止没有新的提交而导致一直waiting
        process_pending_task()

        return success("success")
