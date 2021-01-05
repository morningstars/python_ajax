from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname', '')
        upwd = request.POST.get('upwd', '')
        nickname = request.POST.get('nickname', '')

        models.User.objects.create(uname=uname,
                                   upwd=upwd,
                                   nickname=nickname)
        return HttpResponse('注册成功！')


def reguser(request):
    if request.method == 'GET':
        uname = request.GET.get('uname', '')
        upwd = request.GET.get('upwd', '')
        nickname = request.GET.get('nickname', '')
        try:
            models.User.objects.create(uname=uname,
                                       upwd=upwd,
                                       nickname=nickname)
            return HttpResponse('注册成功')
        except Exception as ex:
            return HttpResponse('注册失败')
    elif request.method == 'POST':
        uname = request.POST.get('uname', '')
        upwd = request.POST.get('upwd', '')
        nickname = request.POST.get('nickname', '')
        try:
            models.User.objects.create(uname=uname,
                                       upwd=upwd,
                                       nickname=nickname)
            return HttpResponse('注册成功')
        except Exception as ex:
            return HttpResponse('注册失败')


def checkuname(request):
    uname = request.GET.get('uname', '')
    users = models.User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse('1')
    return HttpResponse('0')
