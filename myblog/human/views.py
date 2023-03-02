from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
menu = ['House','products','calculate']

def index(request):
    table = students.objects.all()
    return render(request, 'human/index.html', {'title': 'Main page', 'menu': menu, 'table': table})

def temp(request):
    return render(request, 'human/about.html', {'title': 'About site'})

def categories(request, humanID):
    if humanID >= 100:
        return redirect('base', permanent=True)
    return HttpResponse(f"<h1>INNER MAIN</h1><p>{humanID}<p/>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('OK, just leave')
