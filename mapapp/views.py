from django.shortcuts import render, redirect
from .models import Locate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def kakao(request):
    locates = Locate()
    locates.we = request.GET['we']
    locates.ku = request.GET['ku']
    locates.save()
    return render(request, 'kakao.html', {'locates': locates})


def google(request):
    lo = Locate()
    lo.we = request.GET['we']
    lo.ku = request.GET['ku']
    lo.save()
    return render(request, 'google.html', {'locates': lo})
