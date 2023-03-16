from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Auth
from .forms import authForm, RegisterUserForm, LoginUserForm
from django.views.generic import DetailView, CreateView, FormView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class regDetail(DetailView):
#     model = Auth
#     template_name = 'authorization/auth.html'
#     context_object_name = 'auth'
#     allow_empty = False
#     slug_url_kwarg = 'Название слага в views.py'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['file'] = 'file'
#         return context
#
#      def get_queryset(self):
#         return Auth.objects.filter()



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authorization/auth.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')





# def regAuth(request):
#     error = ''
#     if request.method == 'POST':
#         form = authForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Пользователь с таким логином уже существует'
#     else:
#         form = authForm()
#
#     data ={
#         'form': form,
#         'error': error
#     }
#     return render(request, 'authorization/auth.html',data)