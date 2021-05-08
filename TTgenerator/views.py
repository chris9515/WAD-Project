from django.shortcuts import redirect, render
from .models import Teacher, Student
from .forms import CustomUserCreationForm, StudentForm, CustomAuthenticateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .utilities import processFacultyRegistrarionForm, schedulingalgo
from django.contrib import messages
from django.contrib.auth.models import User
import json

# Create your views here.
def TimeTableGenerator(request):
    # context = {"user":request.user}
    return render(request, "TTGen.html",)

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
            return redirect('ttplanner')
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
            return redirect('ttplanner')
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


def create_schedule(request):
    if request.method == 'POST':    
        data  = request.POST
        print(data)
        week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        subjects = request.POST.getlist('subject')
        periods = request.POST.getlist('periods')
        start_time = request.POST.get('startTime')
        end_time = request.POST.get('endTime')
        break_time = request.POST.get('breakTime')
        duration = request.POST.get('breakDuration')
        subject_data = dict()
        for i in range(len(subjects)):  
            subject_data[subjects[i]] = periods[i]
        print(subject_data)
        output,times = schedulingalgo(start_time,end_time,break_time,duration,subject_data)
        list2 = []
        for i in range(len(times)-1):
            hi,mi =times[i].split(":")
            ho,mo = "1:00".split(":")
            hi = int(hi) 
            ho=int(ho)
            mi=int(mi) 
            mo=int(mo)
            h = hi+ho   
            m = mi+mo
            if m>60:
                h+=1
                m=m%60
            if len(str(m))<2 : 
                time1 = str(h)+":"+str(m)+'0'
            else:
                time1 = str(h)+":"+str(m)
            time = times[i] + '-'+ time1
            list2.append(time)
        for i in output.keys():
            output[i] =dict([(value, key) for key, value in output[i].items()])
        # print(output)
        times.pop()
        for i in output.keys():
            for j in times:
                if j in output[i].keys():
                    continue
                else:
                    output[i][j] = ' None'
            output[i]['12:00']='LUNCH'        
        for i in output.keys():
            output[i] = dict(sorted(output[i].items(), key = lambda x : int(x[0].split(":")[0] + x[0].split(":")[1]) ))
        dict(sorted(output.items()))
        return render(request, 'TimetableResponse.html', {'output' : output,'times':times,'list2':list2, 'week':week, 'subjects':subject_data})
    return render(request, 'CreateSchedule.html')

def TimeTablePlannerView(request):
    context = {"user":request.user}

    # if request.method == 'POST':
    #   weeks = request.POST.get('weeks')
    #   week = weeks.strip('][').split(',')
    #   start = request.POST.get('start')
    #   end = request.POST.get('end')
    #   break1 = request.POST.get('break1')
    #   time = request.POST.get('time')
    #   Subjects = request.POST.get('subjects') # '{'Table':Table}'
    #   Subjects = json.loads(Subjects)   # {}
    #   Table,Intervals = TimeTableGenerator(week,start,end,break1,time,Subjects)
      

    #   context['Table'] = Table # context+={"Table":Table}
    #   context['Interval'] = Intervals
    #   context['break1'] = break1
      
    return render(request, 'TimeTablePlanner.html', context)

# def tt(weeks,start,end,break1,time,subjects)
