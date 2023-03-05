from article.views import *
from django.urls import path

urlpatterns = [
    path('',show_article,name='article')
]
