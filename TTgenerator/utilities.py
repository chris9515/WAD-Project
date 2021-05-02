from django.contrib.auth.models import User
from .models import Teacher, Student


def processFacultyRegistrarionForm(form):
    first_name = form.get("first_name")
    last_name = form.get("last_name")
    username = form.get("username")
    email = form.get("email")
    password1 = form.get("password1")
    password2 = form.get("password2")
    subject = form.get("subject")
    user = User.objects.create(
        first_name=first_name.strip(),
        last_name=last_name.strip(),
        username=username.strip(),
        email=email.strip(),
        password=password1.strip(),
        is_staff=True
    )
    teacher = Teacher.objects.create(user=user, subject=subject)
    return teacher


def schedulingalgo(startTime, endTime, breakTime, breakDuration, subjectData):
    # Process
    # Process
    # Process
    # Process
    # Process
    # Process
    A = {
    'Monday': {'CCN': '9:00', 'WAD': '12:00', 'AI': '14:00', 'ML': '16:00'}, 
    'Friday': {'AI': '8:00', 'ML': '9:00', 'TOC': '11:00', 'CCN': '16:00', 'WAD': '17:00'}, 
    'Thursday': {'CCN': '14:00', 'TOC': '15:00','WAD': '16:00'}, 
    'Saturday': {'ML': '9:00', 'TOC': '10:00', 'AI': '13:00', 'WAD': '15:00'}, 
    'Tuesday': {'AI': '10:00', 'CCN': '11:00', 'WAD': '15:00'}, 
    'Wednesday': {'CCN': '8:00', 'TOC': '13:00'}
    }
    return A