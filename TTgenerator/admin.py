from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(MeetingTime)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Room)