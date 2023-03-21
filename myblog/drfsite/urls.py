from django.urls import path
from article.views import articleAPIView

urlpatterns = [
    path('api/v1/artlst', articleAPIView.as_view())
]