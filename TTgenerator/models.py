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
