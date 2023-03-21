
from django.shortcuts import render

def index(request):
    return render(request,'uptrade/base.html', {'page': 'main'})

def cat(request, menu_slug):
    page = menu_slug
    return render(request,'uptrade/base.html', {'page': page})