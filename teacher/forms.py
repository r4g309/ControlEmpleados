from django import forms
from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    nit = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Document number'}),
                             required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full name'}), required=True)
    work_hour = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Hours worked per week'}), required=True)
    value_work = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'how much is each hour of work'}), required=True)

    class Meta:
        model = Teacher
        fields = ('nit', 'name', 'work_hour', 'value_work')
