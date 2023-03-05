from django.shortcuts import render

def show_article(request):
    return render(request, 'article/article.html',)
