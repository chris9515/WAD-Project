from django.db import models

# Create your models here.
class ToDoList(models.Model): #model for daily planner or todo list
    text = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text[:20]
