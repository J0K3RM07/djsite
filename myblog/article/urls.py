from article.views import *
from django.urls import path

urlpatterns = [
    path('',show_article.as_view(),name='article'),
    path('create/',create_article.as_view(),name='create'),
    path('<int:pk>', articalDetail.as_view(), name='artID')
]
