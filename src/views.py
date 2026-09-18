from django.shortcuts import render

# Create your views here.




def imron(request):
    ctx={}
    return render(request, "imron.html")