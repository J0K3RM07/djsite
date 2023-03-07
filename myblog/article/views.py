from django.shortcuts import render,redirect
from .models import article
from .forms import articleForm
from django.views.generic import DetailView

class articalDetail(DetailView):
    model = article
    template_name = 'article/detail_view.html'
    context_object_name = 'art'



def show_article(request):
    art = article.objects.order_by('-date')
    return render(request, 'article/article.html', {'art': art})

def createPost(request):
    error = ''
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')
        else:
            error = "Форма введена не правильно"
    form = articleForm()
    data ={
        'form': form,
        'error': error
    }
    return render(request,'article/create_article.html', data)
