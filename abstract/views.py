
# Create your views here.
from django.shortcuts import render
from .models import *


def home(request, year, chapternum):
    context = {'posts': Chapter_Data.objects.filter(Chapter_Number=chapternum, Year_Published=year)}
    return render(request, './abstract/home.html', context)


def index(request, year):
    context = {'posts': Index_Data.objects.filter(Year_Published=year),
               'ext': Ext_Link.objects.filter(Year_Published=year),
               'messagedata': Year_Data.objects.filter(Year_Published=year),
               'navbar': Navbar.objects.filter(Year_Published=year)
               }
    return render(request, './abstract/index.html', context)


def super(request):
    context = {'posts': Year_Data.objects.all()}
    return render(request, './abstract/super.html', context)


def about(request):
    return render(request, './abstract/about.html')
