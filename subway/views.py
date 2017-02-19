from django.shortcuts import render
from django.views.generic import ListView
import sys
from django.db.models import Q
# from django.utils import timezone

#from datetime import datetime
import datetime
from .models import SubwayModel

import codecs
import operator
# Create your views here.

def SubwayLV(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/busy.html'

    context = {}

    return render(request, template_name, context)

def main(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/index.html'

    context = {}

    return render(request, template_name, context)

def subway_lazy(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/busy.html'


    context = {}

    template_name = 'subway/lazy.html'


    return render(request, template_name, context)

def subway_now(request):
    now = datetime.datetime.now()

    template_name  = 'subway/busy.html'

    template_name='subway/now.html'
    context = {}
    return render(request, template_name, context)


def lanking(request):
    now = datetime.datetime.now()

    template_name  = 'subway/busy.html'


def bsbusy(request):
    context={}
    template_name = 'subway/1bz.html'
    return render(request, template_name, context)

def bsempty(request):
    context = {}
    template_name = 'subway/1bz.html'
    return render(request, template_name, context)

def bsmy(request):
    context = {}
    return render(request, 'subway/3my.html', context)

def bsvs(request):
    return render(request, 'subway/4vs.html')
    #return render(request, 'subway/3rst.html', {'context': context})

def bscm(request):
    return render(request, 'subway/3my.html')

def bsfd(request):
    return render(request, 'subway/6fd.html')
    
def bsch(request):
    return render(request, 'subway/chat.html')
    
def bssh(request):
    return render(request, 'subway/search.html')


