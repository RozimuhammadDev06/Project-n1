from django.urls import path
from .views import t1


from .views import t2



urlpatterns =  [
    path('t1/', t1, name='me'),


    path('t2/', t2, name='me'),
]