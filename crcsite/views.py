from django.shortcuts import render, redirect
from django.template import loader

def index(request):
    return render(request, 'crcsite/index.html')
    
def ra(request):
    return render(request, 'crcsite/ra.html')
    
def raresult(request):
    return render(request, 'crcsite/ra_result.html')
    
def explain(request):
    return render(request, 'crcsite/explain.html')
    
def appo(request):
    return render(request, 'crcsite/appo.html')
    
def screen(request):
    return render(request, 'crcsite/screen.html')
    
def treatment(request):
    return render(request, 'crcsite/treatment.html')
    
def others(request):
    return render(request, 'crcsite/others.html')
    
    