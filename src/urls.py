from django.urls import path
from .views import t1,imron,asliddin


from .views import t2



urlpatterns =  [
    path('imron/', imron, name='Happy'),
    path('t1/', t1, name='me'),
    path('t2/', t2, name='t2'),
    path('asliddin/', asliddin, name='asliddin'),

]

