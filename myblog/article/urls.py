from article.views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',cache_page(60*2)(show_article.as_view()),name='article'),
    path('create/',cache_page(60*2)(create_article.as_view()),name='create'),
    path('<int:pk>', articalDetail.as_view(), name='artID'),
]
