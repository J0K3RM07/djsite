from article.views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',show_article.as_view(),name='article'),
    path('create/',create_article.as_view(),name='create'),
    path('<int:pk>', articalDetail.as_view(), name='artID'),
    path('api/v1/artLst/', articleAPIView.as_view(), name='api'),
]
