from django.shortcuts import redirect, render
from django.views import View

from teacher.models import Teacher
from .forms import TeacherCreateForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'teacher/index.html', context)


class ListTeacherView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'teacher/list_teacher.html', context)


class CreateTeacherView(View):
    def get(self, request, *args, **kwargs):
        form = TeacherCreateForm()

        context = {
            'form': form
        }
        return render(request, 'teacher/create_teacher.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = TeacherCreateForm(request.POST)
            if form.is_valid():
                nit = form.cleaned_data.get('nit')
                name = form.cleaned_data.get('name')
                work_hour = form.cleaned_data.get('work_hour')
                value_work = form.cleaned_data.get('value_work')

                t, created = Teacher.objects.get_or_create(nit=nit, name=name, work_hour=work_hour,value_work=value_work)
                t.save()
                return redirect('teacher:home')
        context = {

        }
        return render(request, 'teacher/create_teacher.html', context)
