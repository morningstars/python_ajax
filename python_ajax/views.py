from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'xhr.html')