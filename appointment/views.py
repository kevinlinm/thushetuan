# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from appointment.models import Ticket, User
import datetime

# Create your views here.
def index(request):
    time_now = datetime.datetime.now()
    time_start = datetime.datetime(2015, 4, 20, 22, 00, 00)
    return render(request, 'appointment/index.html', {
        'time_now': time_now,
        'time_start': time_start,
    })

def nametag(request):
    time_now = datetime.datetime.now()
    time_start = datetime.datetime(2015, 4, 20, 22, 00, 00)
    if time_now > time_start:
        tickets = Ticket.objects.filter(game=1)
        return render(request, 'appointment/nametag.html', {
            'tickets': tickets,
        })
    else:
       return render(request, 'appointment/index.html', {
            'time_now': time_now,
            'time_start': time_start,
       })

def soccer(request):
    time_now = datetime.datetime.now()
    time_start = datetime.datetime(2015, 4, 20, 22, 00, 00)
    if time_now > time_start:
        tickets = Ticket.objects.filter(game=2)
        return render(request, 'appointment/soccer.html', {
            'tickets': tickets,
        })
    else:
        return render(request, 'appointment/index.html', {
            'time_now': time_now,
            'time_start': time_start,
        })

def book(request):
    game = request.GET['game']
    tickets = Ticket.objects.filter(game=game)
    if game == '1':
        renderurl = 'appointment/nametag.html'
    else:
        renderurl = 'appointment/soccer.html'

    try:
        ticket_id = request.POST['choice']
        username = request.POST['username']
        thu_id = request.POST['thu_id']
        tel = request.POST['tel']
    except KeyError:
        return render(request, renderurl, {
            'tickets': tickets,
            'error_message': '请选择一种票',
        })
    else:
        ticket = get_object_or_404(Ticket, pk=ticket_id)

        if ticket.number == 0:
            return render(request, renderurl, {
                'tickets': tickets,
                'error_message': '该时间段的票已售罄',
            })
        else:
            userfilter = User.objects.filter(thu_id=thu_id).first()

            if username == '' or len(thu_id) != 10 or len(tel) != 11:
                return render(request, renderurl, {
                    'tickets': tickets,
                    'error_message': '姓名、学号或电话有误',
                })
            elif userfilter is not None:
                return render(request, renderurl, {
                    'tickets': tickets,
                    'error_message': '一个学号只允许抢一张票',
                })
            else:
                user = User(username=username, thu_id=thu_id, tel=tel, ticket=ticket)
                user.save()
                ticket.number -= 1
                ticket.save()
                return HttpResponseRedirect('/appointment/success/?uid=%s&tid=%s' % (user.id, ticket.id))

def success(request):
    uid = request.GET.get('uid', '0')
    tid = request.GET.get('tid', '0')
    user = get_object_or_404(User, pk=uid)
    ticket = get_object_or_404(Ticket, pk=tid)

    if ticket.time < '12:00-12:15':
        mode = '2v2'
    else:
        mode = '3v3'

    if ticket.game == 1:
        gamename = '海洋球撕名牌'
    else:
        gamename = '泡泡足球'

    context = {
        'username': user.username,
        'thu_id': user.thu_id,
        'time': ticket.time,
        'mode': mode,
        'gamename': gamename,
    }

    return render(request, 'appointment/success.html', context)
