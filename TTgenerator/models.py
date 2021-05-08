from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
#     is_student = models.BooleanField(default=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    # name = models.CharField(max_length=20)
    year = models.DateField(auto_now_add=True)
    # email = models.EmailField()
    def __str__(self):
        return self.user.username
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    # name = models.CharField(max_length=20)
    # email = models.EmailField()
    subject = models.CharField(max_length = 30, default="Maths")
    def __str__(self):
        return self.user.username

# class Period(models.Model):
#     periodLength = models.CharField(max_length=20)
#     period = models.CharField(max_length=20)

# class Timetable(models.Model):

class Instructor(models.Model):
    ID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    def __Str__(self):
        return f'{self.ID}{self.name}'

class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=30)
    instructors = models.ManyToManyField()        