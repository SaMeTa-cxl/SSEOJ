import functools, os, base64, smtplib, random, string

from rest_framework import status
from rest_framework.response import Response
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
            print(request.data)
            s = serializer(data=request.data)
            if s.is_valid():
                return view_method(*args, **kwargs)
            else:
                return _invalid_serializer(s)

        return handle

    return validate


def paginate_data(request, query_set, object_serializer=None):
    """
    :param request: django的request
    :param query_set: django model的query set或者其他list like objects
    :param object_serializer: 用来序列化query set, 如果为None, 则直接对query set切片
    :return:返回分页后的data
    """
    try:
        page_num = int(request.GET.get("page_num", "1"))
    except ValueError:
        page_num = 10
    if page_num < 0 or page_num > 250:
        page_num = 10
    try:
        page_size = int(request.GET.get("page_size", "10"))
    except ValueError:
        page_size = 0
    if page_size < 0:
        page_size = 0
    results = query_set[(page_num - 1) * page_size: page_size * page_num]
    if object_serializer:
        results = object_serializer(results, many=True).data
    return results


class ImageCode:
    @staticmethod
    def image_base64(imagePath):
        if not os.path.exists(imagePath):
            imagePath = 'static/1.png'

        with open(imagePath, 'rb') as pngFile:
            data = pngFile.read()

        encodedString = base64.b64encode(data)

        return encodedString

    @staticmethod
    def base64_image(encodedString, user_id):
        path = 'static/user_' + str(user_id) + '.png'

        imgStr = base64.decodebytes(encodedString.encode('ascii'))
        with open(path, 'wb') as imageFile:
            imageFile.write(imgStr)

        return path


class VerificationCode:
    smtpServer = 'smtp.qq.com' #SMTP服务器配置
    smtpPort = 465 #SMTP服务器端口
    emailUser = '2394160277@qq.com'  #邮箱地址
    emailAuthCode = 'mselvjmiqgbfdjja'  # 授权码
    title = 'SSEOJ验证码'
    messageStr = ['您的注册账号验证码为\n\n', '您的找回密码验证码为\n\n']
    endStr = '\n\n该验证码在3分钟内有效，请及时使用\n如并非您的操作请直接忽略此信息并防止验证码泄露'

    @staticmethod
    def randomCode():
        return ''.join(random.choices(string.digits + string.ascii_uppercase, k=6))

    @staticmethod
    def createMessage(toEmail, title, body):
        msg = MIMEMultipart()
        msg['from'] = VerificationCode.emailUser
        msg['to'] = toEmail
        msg['Subject'] = title

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        return msg

    @staticmethod
    def sendMessage(toEmail, type_code):
        code = VerificationCode.randomCode()
        body = f"Hello, {VerificationCode.messageStr[type_code]}{code}{VerificationCode.endStr}"
        sendState = True

        try:
            # 使用SMTP_SSL连接到QQ邮箱的SMTP服务器
            server = smtplib.SMTP_SSL(VerificationCode.smtpServer, VerificationCode.smtpPort)
            server.login(VerificationCode.emailUser, VerificationCode.emailAuthCode)

            # 发送邮件
            msg = VerificationCode.createMessage(toEmail, VerificationCode.title, body)
            text = msg.as_string()
            server.sendmail(VerificationCode.emailUser, toEmail, text)

        except Exception as e:
            sendState = False
        finally:
            server.quit()

        if sendState:
            return code
        else:
            return None


class DecodePassword:
    @staticmethod
    def GetPassword(encoded):
        decoded = encoded
        return decoded
