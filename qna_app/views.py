from django.db import models
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import QuestionForm
from .models import QuestionModel,AnswerModel,CategoryModel
from django.views.generic import CreateView
from django.views.generic import ListView

class QuestionModelCreateView(CreateView):
    model=QuestionModel
    fields = '__all__'

class QuestionModelListView(ListView):
        model = QuestionModel
        fields = '__all__'



def addquestion(request):
    if request.method =="POST":
        form=QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('Submitted')
            except:
                return HttpResponse('Failed')
        else:
            return HttpResponse(form.errors)

    else:

      # form=QuestionForm()
      category= CategoryModel.objects.all()
      return render(request,'questionmodel_create.html',{'category':category})

def update_question(request,id):
    question = QuestionModel.objects.get(id=id)
    if request.method =="POST":

        form=QuestionForm(request.POST,request.FILES,instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read',id)
            except:
                return HttpResponse('Failed')
        else:
            return HttpResponse(form.errors)

    else:

      form=QuestionForm

      return render(request,'questionmodel_create.html',{'forms':form})

def delete_question(requests,id):
    question= QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')
    # return HttpResponse('Delete successful')

def popular(request):
    question = QuestionModel.objects.all()
    return render(request,'popular.html',{'questions':question})

def question(request):
    question = QuestionModel.objects.all()
    return render(request,'questionmodel_list.htm',{'questions':question})