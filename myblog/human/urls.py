from django.urls import path

from .views import *
urlpatterns = [
    path('human/', index),
    path('human/<int:humanID>/', categories),
    path('about/', temp),
]
