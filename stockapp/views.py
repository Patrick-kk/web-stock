# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from stockapp.serializers import BookSerializer
from stockapp.models import Book
from django.views.decorators.http import require_http_methods
import pytz, datetime
import tushare as ts
import json


def hello(request):
    return HttpResponse("<h1> 爱你~ 小萍 !</h1>")

def getCurTime(request):
    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.datetime.now(tz)
#    today = now.strftime('%Y-%m-%d %H:%M:%S')

    return HttpResponse("time")

@require_http_methods(["GET"])
def getTopList(request):
    response = {}
    try:
        tz = pytz.timezone('Asia/Shanghai')
        now = datetime.datetime.now(tz)
        today = now.strftime('%Y-%m-%d')        
   
    #    today = datetime.date(2018,1,19).strftime('%Y-%m-%d')
        toplist = ts.top_list()
        if toplist.empty:
            response['list'] = []
        else:
            response['list'] = json.loads(toplist.to_json(orient='records', force_ascii=False))
    #    response['list'] = toplist
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = e
        response['eror_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = BookSerializer(books, many=True).data
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = str(e)
        response['error_num'] = 1
		
    return JsonResponse(response)
