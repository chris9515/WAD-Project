from django import forms
from .models import ToDoList

# class TodoForm(forms.Form):
#     text = forms.CharField(label="Text", max_length=300, help_text="Enter your notes")

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('text','completed')