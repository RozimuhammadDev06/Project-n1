from django.shortcuts import render
from .models import Oquvchi
# Create your views here.




def imron(request):
    ctx={}
    return render(request, "imron.html")





def t1(request):
    oquvchi = Oquvchi.objects.all()
    oquvchi_soni = Oquvchi.objects.count()

    ctx={
        'oq':oquvchi,
        "soni": oquvchi_soni,
    }
    return render(request, "t1.html",ctx)







def t2(request):
    ctx={}
    return render(request, "t2.html")




def asliddin(request):
    ctx={}
    return render(request, "aslidin.html")