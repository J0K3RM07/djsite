from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', index, name='menu'),
    path('menu/<slug:menu_slug>', cat, name='advmenu')
]