from django.urls import path

from .views import *
urlpatterns = [
    path('human/', index, name='base'),
    path('human/<int:humanID>/', categories)
]
