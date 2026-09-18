from django.shortcuts import render

# Create your views here.




def t1(request):
    ctx={}
    return render(request, "t1.html")