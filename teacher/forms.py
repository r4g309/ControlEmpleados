from django import forms
from .models import Teacher

class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('nit','name','work_hour','value_work')
        