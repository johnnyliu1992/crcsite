from django.shortcuts import render, redirect
from django.template import loader
from .forms import CRC

def index(request):
    return render(request, 'crcsite/index.html')
    
def ra(request):
    form=CRC()

    return render(request, 'crcsite/ra.html', {'form': form})
    
def raresult(request):
    if request.method=='GET':
        q12=float(request.GET.get('q12'))
        q13=float(request.GET.get('q13'))
        q21=float(request.GET.get('q21'))
        q22=float(request.GET.get('q22'))
        q23=float(request.GET.get('q23'))
        q24=float(request.GET.get('q24'))
        q25=float(request.GET.get('q25'))
        q31=float(request.GET.get('q31'))
        q32=float(request.GET.get('q32'))
        q33=float(request.GET.get('q33'))
        score=q12*q13*q21*q22*q23*q24*q25*q31*q32*q33
        min=0.72
        max=6.95
        score=((score-min)/(max-min))*10
        score=round(score, 2)
        level=22222
        if score >= 6:
            level="High"
        elif score <= 4:
            level="Low"
        else:
            level="Normal"
        return render(request, 'crcsite/ra_result.html', {'score': score, 'level': level})
    else:
        n="No"
        return render(request, 'crcsite/ra_result.html', {'n': n})
    
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
    
    