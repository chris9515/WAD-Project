from django.db import models

# Create your models here.
class ToDoList(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text[:20]
