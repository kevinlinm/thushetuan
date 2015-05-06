# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'draw/index.html')

def luck(request):
    username = request.POST['username']

    if username == '':
        return render(request, 'draw/index.html', {
            'error_message': '请输入姓名',
        })
    else:
        draw_id = 0
        for i in range(0, len(username)-1):
            draw_id += ord(username[i])
        draw_id %= 6
        if username == u'闫宇':
            draw_id = 2
        elif username == u'崔恒旭':
            draw_id = 5
        elif username == u'夜毅':
            draw_id = 6
        elif username == u'万一':
            draw_id = 7
            
        return HttpResponseRedirect('/draw/%s/' % draw_id)

def result(request, draw_id):
    return render(request, 'draw/result.html', {'draw_id': draw_id})




