from django import forms
from .models import Student, Teacher
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.admin import User
from django.forms import ModelForm

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields=['username','password1','password2','is_staff']
# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','username', 'email','is_staff','password1', 'password2')

class StudentForm(UserCreationForm):
    year = forms.DateField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]

class CustomUserCreationForm(UserCreationForm):
    # subject = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1', 'password2',]

class CustomAuthenticateForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'username'})
        self.fields['password'].widget = forms.TextInput(attrs={'placeholder' : 'password', 'type' : 'password'})