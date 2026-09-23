from django.shortcuts import render
from  .models import Oquvchi,Maktab,Sinf
# Create your views here.




def imron(request):
    ctx={}
    return render(request, "imron.html")





def t1(request):
    ctx={}
    return render(request, "t1.html")







def t2(request):
    ctx={}
    return render(request, "t2.html")




def asliddin(request):
    oquvchi = Oquvchi.objects.all()
    oquvchi_soni = oquvchi.count()
    maktab = Maktab.objects.all()
    sinf = Sinf.objects.all()
    ctx={
        "oq": oquvchi,
        "soni": oquvchi_soni,
        "maktab": maktab,
        "sinf": sinf,
    }
    return render(request, "aslidin.html", ctx)