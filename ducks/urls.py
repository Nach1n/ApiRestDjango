from django.conf.urls import url
from ducks.views import *
from django.urls import path

urlpatterns = [
    path('ducks/', DuckList.as_view(), name='ducks'),
]