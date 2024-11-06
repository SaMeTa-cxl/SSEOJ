import functools
import json

from django.http import HttpResponse, QueryDict, JsonResponse
from django.views.generic import View


class ContentType(object):
    json_request = "application/json"
    json_response = "application/json;charset=UTF-8"
    url_encoded_request = "application/x-www-form-urlencoded"
    binary_response = "application/octet-stream"


class ApiView(View):
    @staticmethod
    def success(data=None):
        """
        :param data: 需要返回的数据，类型为json支持的类型：字符串、数值、字典、列表等
        :return: 一个JsonResponse，错误为None，数据为data
        对JsonResponse的封装，表示成功处理，并将处理结果放在data中
        """
        return JsonResponse({"error": None, "data": data})

    @staticmethod
    def error(msg="error", err="error"):
        """
        :param msg: 一个字符串，错误信息
        :param err: 一个字符串，错误类型
        :return: 一个JsonResponse，将错误类型和错误信息以Json格式返回
        """
        return JsonResponse({"error": err, "data": msg})

    def extract_errors(self, errors, key="", full_key=""):
        """
        :param errors: serializer.errors，为一个字典（可能有嵌套结构），保存了字段校验错误的信息
        :param key: 保存了当前层错误的字段
        :param full_key: 保存了完整的错误字段
        :return: 一个元组，完整错误字段及其错误信息
        该函数将serializer.errors拆解，返回第一个错误的字段及其错误信息
        例：若有errors如下：
        errors = {
            "user": {
                "profile": {
                    "bio": ["This field may not be blank."]
                }
            }
        }
        则将返回("user-profile-bio", "This field may not be blank.")
        """
        if isinstance(errors, dict):
            key = list(errors.keys())[0]
            full_key += key + '-'
            return self.extract_errors(errors.pop(key), key, full_key)
        elif isinstance(errors, list):
            return self.extract_errors(errors[0], key, full_key)

        return full_key[0: -1], errors

    def invalid_serializer(self, serializer):
        """
        :param serializer: 一个序列化器，需要从它获取错误信息
        :return: 以JsonResponse形式返回序列化器的错误字典中的第一个错误信息
        """
        key, error = self.extract_errors(serializer.errors)
        if key == "non-field-errors":
            msg = error
        else:
            msg = f"{key}: {error}"
        return self.error(err=f"invalid-{key}", msg=msg)


def validate_serializer(serializer):
    """
    :param serializer: 一个序列化器
    :return: 被装饰好的函数
    一个装饰器，用于简化重复的验证代码，对请求数据进行验证，如果验证通过则继续对请求进行处理，
    若验证失败，则不再继续处理请求，而是调用invalid_serializer返回验证失败的具体信息
    """
    def validate(view_method):
        @functools.wraps(view_method)
        def handle(*args, **kwargs):
            self = args[0]
            request = args[1]
            s = serializer(data=request.data)
            if s.is_valid():
                request.data = s.data
                request.serializer = serializer
                return view_method(*args, **kwargs)
            else:
                return self.invalid_serializer(s)

        return handle

    return validate
