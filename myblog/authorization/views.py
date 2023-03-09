from django.shortcuts import render, redirect
from .models import Auth
from .forms import authForm
from django.views.generic import DetailView


#class authDetail(DetailView):
    # model = auth
    #template_name = 'authorization/auth.html'
    #context_object_name = 'auth'




def regAuth(request):
    error = ''
    if request.method == 'POST':
        form = authForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Пользователь с таким логином уже существует'
    else:
        form = authForm()

    data ={
        'form': form,
        'error': error
    }
    return render(request, 'authorization/auth.html',data)