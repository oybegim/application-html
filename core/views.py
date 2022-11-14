from django.shortcuts import render

from frontend import *

def asosiy1(request):
    return render(request, 'gul.html')
def asosiy2(request):
    return render(request, 'meva.html')
def cube(request):
    return render(request,'cube.html')        
