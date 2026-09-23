from django.shortcuts import render



from .models import Oquvchi,Maktab,Sinf

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
    oquvchi = Oquvchi.objects.all()
    maktab = Maktab.objects.all()
    sinf = Sinf.objects.all()
    oquvchi_soni = Oquvchi.objects.count()
    ctx={
    'oq':oquvchi,
    "soni":oquvchi_soni,
    "mk":maktab,
    "si":sinf,
    }
    return render(request, "t2.html", ctx)




def asliddin(request):
    ctx={}
    return render(request, "aslidin.html")