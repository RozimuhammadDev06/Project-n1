from django.urls import path
from .views import t1,imron


from .views import t2



urlpatterns =  [
    path('imron/', imron, name='Happy'),
    path('t1/', t2, name='me'),
    path('t2/', t1, name='t2'),
]

