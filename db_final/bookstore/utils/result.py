from django.http import HttpResponse
import time
import json

def ok(result):
    ret = {
        'msg': "一切OK",
        'code': 200,
        'data': {},
        'timestamp': time.strftime('yyyy-MM-dd hh:mm:ss', time.localtime()),
        'success': True
    }
    ret['data'] = result
    return HttpResponse(json.dumps(ret), content_type='application/json,charset=utf-8')

def error(msg):
    ret = {
        'msg': "发生错误",
        'code': 500,
        'data': {},
        'timestamp': time.strftime('yyyy-MM-dd hh:mm:ss', time.localtime()),
        'success': True
    }
    ret['success'] = False
    ret['msg'] = msg
    return HttpResponse(json.dumps(ret), content_type='application/json,charset=utf-8')

