import hashlib
import os

from django.contrib.messages.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from werkzeug.utils import secure_filename

from conf.conf import SysConfigs
from conf.serializers import JudgeServerHeartbeatSerializer
from judge.models import JudgeServer
from utils.api import validate_serializer, success, fail
from judge.dispatcher import process_pending_task


class JudgeServerHeartbeatAPI(APIView):
    @validate_serializer(JudgeServerHeartbeatSerializer)
    def post(self, request):
        data = request.data
        client_token = request.META.get("HTTP_X_JUDGE_SERVER_TOKEN")
        if hashlib.sha256(SysConfigs.judge_server_token.encode("utf-8")).hexdigest() != client_token:
            return JsonResponse({'msg': "Invalid token", 'error': 'error'})

        try:
            server = JudgeServer.objects.get(hostname=data["hostname"])
            server.judger_version = data["judger_version"]
            server.cpu_core = data["cpu_core"]
            server.memory_usage = data["memory"]
            server.cpu_usage = data["cpu"]
            server.service_url = data["service_url"]
            server.last_heartbeat = timezone.now()
            server.save(update_fields=["judger_version", "cpu_core", "memory_usage", "service_url", "ip", "last_heartbeat"])
        except JudgeServer.DoesNotExist:
            JudgeServer.objects.create(hostname=data["hostname"],
                                       judger_version=data["judger_version"],
                                       cpu_core=data["cpu_core"],
                                       memory_usage=data["memory"],
                                       cpu_usage=data["cpu"],
                                       service_url=data["service_url"],
                                       last_heartbeat=timezone.now(),
                                       )
        # 新server上线 处理队列中的提交，防止没有新的提交而导致一直waiting
        # process_pending_task()

        return JsonResponse({"error": None, "data": 'success'})


class UploadImageAPI(APIView):
    def post(self, request):
        UPLOAD_FOLDER = 'static/image'
            # 检查请求是否包含文件
        if 'image' not in request.FILES:
            return JsonResponse({'status': 400, 'error': 'No file part'}, status=400)

        file = request.FILES['image']
        print(file)

        if file.name == '':
            return JsonResponse({'status': 400, 'error': 'No selected file'}, status=400)

        if file and file.name.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}:
            # 使用安全文件名并保存文件
            filename = secure_filename(file.name)
            filepath = "{}/{}".format(UPLOAD_FOLDER, filename)
            with open(filepath, 'wb+') as destination:
                for chunk in file.chunks():  # 分块写入，处理大文件
                    destination.write(chunk)
            # 构建文件的访问 URL
            file_url = f"http://localhost:8000/{UPLOAD_FOLDER}/{filename}"
            return JsonResponse({'status': 200, 'success': 'Upload success!', 'data': {'link': file_url}})

        return JsonResponse({'status': 400, 'error': 'File type not allowed'}, status=400)

