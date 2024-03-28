from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'header.html')

def service(request):
    return render(request,'service.html')

def work(request):
    return render(request,'work.html')
def working(request):
    return render(request,'working-on-that.html')
#Contact section email sending function-

