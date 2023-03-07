from article.views import *
from django.urls import path

urlpatterns = [
    path('',show_article,name='article'),
    path('create/',createPost,name='create'),
    path('<int:pk>', articalDetail.as_view(), name='artID')
]
