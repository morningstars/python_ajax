from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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


def checkuname(request):
    uname = request.GET.get('uname', '')
    users = models.User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse('用户名称已存在')
    return HttpResponse('通过')
