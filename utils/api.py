import functools

from rest_framework import status
from rest_framework.response import Response


def success(data):
    """
    业务逻辑成功执行时返回的结果，data中err字段为none，data中才是实际的数据
    """
    return Response(data={"err": None, "data": data}, status=status.HTTP_200_OK)


def fail(msg="error", err="error"):
    """
    :param msg: 业务逻辑错误的详细信息
    :param err: 业务逻辑错误的类型
    业务逻辑错误时返回类型和具体信息,注意状态码为200
    """
    return Response(data={"err": err, "msg": msg}, status=status.HTTP_200_OK)


def _extract_errors(errors, key="", full_key=""):
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
        return _extract_errors(errors.pop(key), key, full_key)
    elif isinstance(errors, list):
        return _extract_errors(errors[0], key, full_key)

    return full_key[0: -1], errors


def _invalid_serializer(serializer):
    """
    :param serializer: 一个序列化器，需要从它获取错误信息
    :return: 返回序列化器的错误字典中的第一个错误信息，err字段为错误类型，msg字段为具体错误信息，注意状态码为400
    """
    key, error = _extract_errors(serializer.errors)
    if key == "non-field-errors":
        msg = error
    else:
        msg = f"{key}: {error}"

    response_data = {
        "err": f"invalid-{key}",
        "msg": msg
    }

    return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)


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
            request = args[1]
            s = serializer(data=request.data)
            if s.is_valid():
                return view_method(*args, **kwargs)
            else:
                return _invalid_serializer(s)

        return handle

    return validate
