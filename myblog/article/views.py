from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import article
from .forms import articleForm
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import articleSerializer
from rest_framework import generics, viewsets


# class articleAPIView(generics.ListCreateAPIView):
#
#     queryset = article.objects.all( )
#     serializer_class = articleSerializer

class articleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleSerializer


class create_article(LoginRequiredMixin, CreateView):
    form_class = articleForm
    template_name = 'article/create_article.html'
    success_url = reverse_lazy('article')
    login_url = reverse_lazy('auth')

class articalDetail(DetailView):
    model = article
    template_name = 'article/detail_view.html'
    context_object_name = 'art'

class show_article(ListView):
    model = article
    template_name = 'article/article.html'
    context_object_name = 'art'
    ordering = ['-date']
    paginate_by = 3

# def show_article(request):
#     art = article.objects.order_by('-date')
#     return render(request, 'article/article.html', {'art': art})

# def createPost(request):
#     error = ''
#     if request.method == 'POST':
#         form = articleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article')
#         else:
#             error = "Форма введена не правильно"
#     form = articleForm()
#     data ={
#         'form': form,
#         'error': error
#     }
#     return render(request,'article/create_article.html', data)
