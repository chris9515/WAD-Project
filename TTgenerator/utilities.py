from django.contrib.auth.models import User
from .models import Teacher,Student


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
        is_staff = True
    )
    teacher = Teacher.objects.create(user=user,subject=subject)
    return teacher

