from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.core import serializers
import json

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


def query_users(request):
    return render(request, 'query.html')


def query_server(request):
    users = models.User.objects.all()

    str = serializers.serialize('json', users)

    # msg = ''
    # for u in users:
    #     msg += '%s_%s_%s_%s|' % (u.id, u.uname, u.upwd, u.nickname)
    # msg = msg[0:-1]
    return HttpResponse(str)


def jso(request):
    return render(request, 'jso.html')


def json_views(request):
    return render(request, 'json.html')


def json_server(request):
    dict = {
        'uname': 'zhangsan',
        'uage': 30,
        'ugender': 'MALE'
    }

    import json

    # 使用python的json模块中的dumps()方法转成json字符串
    jsonstr = json.dumps(dict)

    users = [
        {
            'uname': 'zhangsan',
            'uage': 30
        }, {
            'uname': '张三',
            'uage': 30
        }
    ]
    jsonarr = json.dumps(users)

    # 使用django的serializers
    from django.core import serializers

    users = models.User.objects.all()
    str = serializers.serialize('json', users)

    return HttpResponse(str)


def front_json(request):
    return render(request, 'front_json.html')


def front_server(request):
    params = request.GET.get('params', '')
    print(params)
    dict = json.loads(params)
    print(dict)
    msg = '姓名：%s, 年龄：%s，性别：%s' % (dict['uname'], dict['uage'], dict['ugender'])
    return HttpResponse(msg)


def load_views(request):
    return render(request, '01-load.html')
