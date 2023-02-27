from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse(f'<h1>MAIN</h1>')

def categories(request, humanID):
    if humanID >= 100:
        return redirect('base', permanent=True)
    return HttpResponse(f"<h1>INNER MAIN</h1><p>{humanID}<p/>")

def newMetod(request):
    return HttpResponse('<h2>OUTER MAIN<h2\>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('OK, just leave')

def RedirecToMain(request):
    return redirect('base', permanent=True)
