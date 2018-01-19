from django.shortcuts import render, redirect
from django.template import loader
from .forms import CRC, QuestionForm
from crcsite.models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def index(request):
    return render(request, 'crcsite/index.html')
    
def ra(request):
    form=CRC()
    Q1=Question.objects.filter(Q_category='Heredity and medical history').values()
    #l=list(Question.objects.filter(Q_category='Heredity and medical history').values_list('Q_ID', flat=True))
    A=Answer.objects.all()
    #for i in l:
        #A1.append(Answer.objects.filter(Q_ID=i).values())
    
    return render(request, 'crcsite/ra.html', {'Q1': Q1, 'A': A, 'form': form})
    
def raresult(request):
    if request.method=='GET':
        rwc=request.GET.get('relative_with_cancer')
        if rwc == '':
            rwc=0
        else:
            rwc=float(rwc)
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
        #prepare score
        score=q12+q13+q21+q22+q23+q24+q25+q31+q32+q33+0.5*rwc
        min=9.4
        max=12.3+0.5*rwc
        score=((score-min)/(max-min))*10
        score=round(score, 2)
        #preppare level
        level=22222
        if score >= 6:
            level="High"
        elif score <= 4:
            level="Low"
        else:
            level="Normal"
        request.session['score']=score
        #prepare risks factors
        risks=[]
        if q12 != 1:
            risks.append('Inflammatory Bowel Disease')
        else: pass
        if q13 != 1:
            risks.append('Diabetes')
        else: pass
        if q21 != 1:
            risks.append('Alcohol Consumption')
        else: pass
        if q22 != 1:
            risks.append('Obesity')
        else: pass
        if q23 != 1:
            risks.append('Red Meat Consumption')
        else: pass
        if q24 != 1:
            risks.append('Processed Meat Consumption')
        else: pass
        if q25 != 1:
            risks.append('Smoke')
        else: pass
        
        #show=[{'title':'Risk Level', 'ranges':[1,2,3,4,5,6,7,8,9,10], 'measures':[score], 'markers':[score]}]
        return render(request, 'crcsite/ra_result.html', {'score': score, 'level': level, 'risks': risks})
    else:
        n="No"
        return render(request, 'crcsite/ra_result.html', {'n': n})
    
def explain(request):
    return render(request, 'crcsite/explain.html')
    
def appo(request):
    return render(request, 'crcsite/appo.html')
    
def appoconfirm(request):
    return render(request, 'crcsite/appoconfirm.html')

    
def screen(request):
    return render(request, 'crcsite/screen.html')
    
def treatment(request):
    return render(request, 'crcsite/treatment.html')
    
def others(request):
    return render(request, 'crcsite/others.html')
    
def jfj(request):
    score=request.session.get('score')
    final=[{'title':'Risk Level','subtitle':'in total', 'ranges':[1,2,3,4,5,6,7,8,9,10], 'measures':[score], 'markers':[score]}]
    #final.append({'title':'Risk Level','subtitle':'by risk factors', 'ranges':[1,2.07], 'measures':[0], 'markers':[score]})
    return JsonResponse(final, safe=False)
    
    