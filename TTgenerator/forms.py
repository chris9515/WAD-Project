from django import forms
from .models import *
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

#Forms for various models created, the fields displayed here are the fields going to be displayed in the website

class StudentForm(UserCreationForm): #student form
    year = forms.DateField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]

class CustomUserCreationForm(UserCreationForm): #form for user model
    # subject = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1', 'password2',]

class CustomAuthenticateForm(AuthenticationForm): #form used  for authenticating into a user profile
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'username'})
        self.fields['password'].widget = forms.TextInput(attrs={'placeholder' : 'password', 'type' : 'password'})

class RoomForm(ModelForm): #form for room 
    class Meta:
        model = Room
        fields = [
            'roomNo',
            'capacity'
        ]


class InstructorForm(ModelForm): #form for faculty/instructor
    class Meta:
        model = Instructor
        fields = [
            'instructorID',
            'name'
        ]


class MeetingTimeForm(ModelForm): #form for meeting times
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }


class CourseForm(ModelForm): #form for course 
    class Meta:
        model = Course
        fields = ['courseID', 'courseName', 'maxStudents', 'instructors']


class DepartmentForm(ModelForm): #form for department
    class Meta:
        model = Department
        fields = ['deptName', 'courses']


class SectionForm(ModelForm): #form for section
    class Meta:
        model = Section
        fields = ['sectionID', 'department', 'noClassesInWeek']
