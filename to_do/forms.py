from django import forms
from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    todo      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your Task here "}))
    last_date = forms.DateField(label='' ,widget=forms.SelectDateWidget)


    class Meta:
        model = Todo
        fields = '__all__'


