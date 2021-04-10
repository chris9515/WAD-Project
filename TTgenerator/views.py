from django.shortcuts import redirect, render
from .models import Teacher, Student
from .forms import CustomUserCreationForm, StudentForm, CustomAuthenticateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .utilities import processFacultyRegistrarionForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def TimeTableGenerator(request):
    context = {"user":request.user}
    return render(request, "TTGen.html", context)

def InstituteUse(request):
    return render(request, 'InstituteUse.html')

def PersonnalUse(request):
    return render(request, 'PersonnalUse.html')

def FacultyRegister(request):
    profile = CustomUserCreationForm(initial={'is_staff':True})
    if request.method == 'POST':
        profile = CustomUserCreationForm(request.POST)
        if profile.is_valid():
            # new_teacher = processFacultyRegistrarionForm(request.POST)
            new_teacher = profile.save(commit=False)
            new_teacher.is_staff = True
            new_teacher.save()
            subject = request.POST.get("subject")
            teacher = Teacher.objects.create(user=new_teacher, subject=subject)
            return redirect('facultyLogin')
    return render(request, 'FacultyRegister.html', {"form":profile, 'type':'Faculty'})

def StudentRegister(request):
    profile = CustomUserCreationForm(initial={'is_staff':False})
    if request.method == 'POST':
        profile = CustomUserCreationForm(request.POST)
        if profile.is_valid():
            # new_teacher = processFacultyRegistrarionForm(request.POST)
            new_student = profile.save(commit=False)
            new_student.is_staff = False
            new_student.save()
            year = request.POST.get("year")
            student = Student.objects.create(user=new_student, year=year)
            return redirect('studentLogin')
    return render(request, 'StudentRegister.html', {"form":profile, 'type':'Student'})

def FacultyLogin(request):
    form = CustomAuthenticateForm()
    if request.method == 'POST':
        form = CustomAuthenticateForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.is_staff==True:
            login(request, user)
            return redirect('TTGenerator')
        else:
            messages.info(request, "Username or Password is incorrect!!")
            return render(request, 'FacultyLogin.html', {'form': form, 'type':'faculty'})
    return render(request, 'FacultyLogin.html', {'form': form,'type':'faculty'})

def StudentLogin(request):
    form = CustomAuthenticateForm()
    if request.method == 'POST':
        form = CustomAuthenticateForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.is_staff==False:
            login(request, user)
            return redirect('TTGenerator')
        else:
            messages.info(request, "Username or Password is incorrect!!")
            return render(request, 'StudentLogin.html', {'form': form, 'type':'student'})
    return render(request, 'StudentLogin.html', {'form': form,'type':'student'})

def teacherProfileView(request):
    # user = User.objects.get(username=username)
    profile = Teacher.objects.get(user=request.user)
    return render(request, 'profile.html', {"profile":profile,})

def studentProfileView(request):
    print(request.user)
    profile = Student.objects.get(user=request.user)
    return render(request, 'profile.html', {"profile":profile,})

def logoutView(request):
    logout(request)
    return redirect('InstituteUse')