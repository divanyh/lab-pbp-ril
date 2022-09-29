from sqlite3 import Date
from tkinter import Label
from django import forms
from todolist.models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        widgets = {
            # 'date' : forms.DateInput(),
            'title' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'Insert your task', 'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'type' : 'textarea', 'placeholder' : 'Insert your task details', 'class' : 'form-control'})
            }

        title = forms.CharField(label = 'Title', required = True, widget = widgets['title'])
        description = forms.CharField(label = 'Description', required = True, widget = widgets['description'])