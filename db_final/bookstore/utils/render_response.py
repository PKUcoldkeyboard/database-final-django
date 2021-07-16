from rest_framework.renderers import JSONRenderer
import time


class CustomRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        msg = "访问成功"
        code = 200
        success = True
        if data and isinstance(data, dict) and 'exception' in data:
            code = data['code']
            msg = data['message']
            success = False
        ret = {
            'message': msg,
            'code': code,
            'data': data,
            'timestamp': time.strftime(r'%Y-%m-%d %H:%M:%S', time.localtime()),
            'success': success
        }

        return super().render(ret, accepted_media_type, renderer_context)