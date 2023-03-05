from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *



def index(request):
    return render(request, 'human/mainpage.html',{'title': 'Главная страница'} )

def about(request):
    return render(request, 'human/Aboutsite.html',{'title': 'О сайте'})
