from sqlite3 import Date
from django import forms
from todolist.models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            # 'date' : forms.DateInput(),
            'title' : forms.TextInput(attrs={'placeholder' : 'Insert your task', }),
            'detail' : forms.Textarea(attrs={"placeholder" : 'Insert your task details'})
            }