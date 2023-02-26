from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Создана страница")

def categories(request):
    return  HttpResponse("<h1>Статья по категории</h1>")

# Create your views here.
