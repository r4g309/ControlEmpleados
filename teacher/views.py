from django.shortcuts import render
from django.views import View

from teacher.models import Teacher
from .forms import TeacherCreateForm

class HomeView(View):
    def get(self,request,*args, **kwargs):
        context = {

        }
        return render(request,'index.html',context)

class ListTeacherView(View):
    def get(self,request,*args, **kwargs):
        context={

        }
        return render(request,'list_teacher.html',context)

class CreateTeacherView(View):
    def get(self, request,*args, **kwargs):
        form= TeacherCreateForm()

        context={
            'form':form
        }
        return render(request,'create_teacher.html',context)
    def post(self, request,*args, **kwargs):
        if request.method=="POST":
            form = TeacherCreateForm(request.POST)
            if form.is_valid():
                nit = form.cleaned_data.get('nit')
                name = form.cleaned_data.get('name')
                work_hour = form.cleaned_data.get('work_hour')
                value_work = form.cleaned_data.get('value_work')

                p, created = Teacher.objects.get_or_create()
        context={

        }
        return render(request,'create_teacher.html',context)