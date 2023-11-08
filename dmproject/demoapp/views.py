from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


# Create your views here.
def home(request):
    obj=Place.objects.all()
    objs = Team.objects.all()
    return render(request,'index.html',{'result':obj,'results':objs})




# def operation(request):
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,'result.html',{'res1':add,'res2':sub,'res3':mul,'res4':div})

