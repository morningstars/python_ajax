from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'xhr.html')


def ajax_get(request):
    return HttpResponse('ajax_get返回')


def ajax_show(request):
    return HttpResponse('welcome:' + request.GET.get('name', ''))
