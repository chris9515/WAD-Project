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

time_slots = (
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('10:30 - 11:30', '10:30 - 11:30'),
    ('11:30 - 12:30', '11:30 - 12:30'),
    ('12:30 - 1:30', '12:30 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)
DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

class Instructor(models.Model):
    instituteID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.instituteID} {self.name}'

class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=30)
    maxStudents = models.CharField(max_length=100)
    instructors = models.ManyToManyField(Instructor)
    def __str__(self):
        return f'{self.courseID} {self.courseName}'

class Room(models.Model):
    roomNo = models.CharField(max_length=10)
    capacity = models.IntegerField(default=0)
    def __str__(self):
        return self.roomNo

class Department(models.Model):
    deptName = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    @property
    def get_courses(self):
        return self.courses

    def __str__(self):
        return self.deptName

class MeetingTime(models.Model):
    pid = models.CharField(max_length=4, primary_key=True)
    time = models.CharField(max_length=50, choices=time_slots, default='11:30 - 12:30')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.pid} {self.day} {self.time}'

class Section(models.Model):
    sectionID = models.CharField(max_length=25, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    noClassesInWeek = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    meetingTime = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)

    def set_room(self, room):
        section = Section.objects.get(pk = self.section_id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(pk = self.section_id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.section_id)
        section.instructor = instructor
        section.save()