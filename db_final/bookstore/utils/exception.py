from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    resp = exception_handler(exc, context=context)
    message = "服务器错误!"
    for index, value in enumerate(resp.data):
        if index == 0:
            key = value
            value = resp.data[key]
            if isinstance(value, str):
                message = value
            else:
                message = key + value[0]
    if resp is None:
        return Response({
            'message': '服务器错误'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    else:
        # print('123 = %s - %s - %s' % (context['view'], context['request'].method, exc))
        return Response({
            'message': message,
            'code': resp.status_code,
            'exception': True,
        }, status=resp.status_code, exception=True)