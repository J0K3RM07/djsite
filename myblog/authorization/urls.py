from authorization.views import *
from django.urls import path

urlpatterns = [
    path('', regAuth, name='auth')
]