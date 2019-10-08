from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Food,Choice
from django.urls import reverse

def index(request):
    Qlist=Food.objects.all()
    context={'food_question':Qlist}
    
    return render(request,'vote/index.html',context)
# Create your views here.
def detail(request,Qid):
    try:
        Qdetail=Food.objects.get(pk=Qid)
        
    except:
        return Http404('Nothing is here')
    return render(request,'vote/details.html',{'data':Qdetail})
def result(request,Qid):
    Qdetails=get_object_or_404(Food,pk=Qid)
    return render(request,'vote/result.html',{'data1':Qdetails})

def vote(request,Qid):
    Question=get_object_or_404(Food,pk=Qid)
    try:
        selectc=Question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'vote/details.html',{'data1':Question,'error':"You Didn't select any choice"})
    else:
        selectc.count=selectc.count+1
        selectc.save()
        return HttpResponseRedirect(reverse('vote:result',args=(Question.id,)))