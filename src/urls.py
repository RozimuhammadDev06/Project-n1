from django.urls import path
from .views import t1



urlpatterns =  [
    path('t1/', t1, name='me'),
]