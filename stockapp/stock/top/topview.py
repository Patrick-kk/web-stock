# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import pytz, datetime
import tushare as ts
import json

@csrf_exempt
@require_http_methods(["POST"])
def getTopList(request):
    '''
    前端传过来的 date 实际是该日期的总秒数
    '''
    response = {}
    try:
        timestamp = json.loads(request.body).get('date')
        if not timestamp:
            toplist = ts.top_list()
        else:
            timeformat = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            toplist = ts.top_list(timeformat)
        if toplist.empty:
            response['list'] = []
        else:
            response['list'] = json.loads(toplist.to_json(orient='records', force_ascii=False))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = e
        response['eror_num'] = 1

    return JsonResponse(response)
