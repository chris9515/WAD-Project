from django.contrib.auth.models import User
from .models import Teacher, Student
import random, json


def processFacultyRegistrarionForm(form): #used for registering faculty
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


def schedulingalgo(startTime, endTime, breakTime, breakDuration, subjectData): #additional algorithm for generating timetable
    
    start = startTime
    end = endTime
    break1 = breakTime
    time = "1:00"
    Subjects = subjectData
    lunch_start = '12:00'
    lunch_end = '13:00'

    print(start, end, break1, time)
    week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    weeks = list(week)
    Period = {}

    for i in Subjects.keys():
        n = int(Subjects[i])
        list1 = []
        while n>0:
            rand = random.randint(0,len(week)-1)
            if int(Subjects[i])<len(week) and weeks[rand] in list1 :
                continue
            list1.append(weeks[rand]) 
            n-=1
        Period[i] =  list1.copy()

    Table={}
    for i in weeks :
        list2=[]
        for j in Period.keys():
            while i in Period[j] :
                list2.append(j)
                Period[j].remove(i)
        Table[i]=list2.copy()

    hi,mi = str(start).split(":")
    ho,mo = str(end).split(":")
    h,m = str(break1).split(":")
    hb,mb = str(time).split(":")
    hls,mls = lunch_start.split(":")
    hle,mle = lunch_end.split(":")
    lunch_s = int(hls+mls)
    lunch_e = int(hle+mle)
    begin = int(hi+mi)
    stop = int(ho+mo)
    interval = int(h+m)
    break2 = int(hb+mb)

    list6 = [*range(begin,lunch_s+1,interval+break2)]
    list7 = [*range(lunch_e,stop+1,interval+break2)]
    list3 = list6+list7


    TimeTable={}
    status=0
    
    for i in Table.keys():
        Schedule={}
        list4 = list3.copy()
        if len(list3)-1 < len(Table[i]):
            status=1
            break
        for j in Table[i]:
            rand = random.randint(0,len(list4)-2)
            if len(str(list4[rand]%100)) < 2 :
                Schedule[j]= str(int(list4[rand]/100)) +":"+str(list4[rand]%100)+str(0)
            else :  
                Schedule[j]= str(int(list4[rand]/100)) +":"+ str(list4[rand]%100)
            list4.remove(list4[rand])

            TimeTable[i] = dict(sorted(Schedule.items(), key = lambda x : int(x[1].split(":")[0] + x[1].split(":")[1]) ))
    list5=[]
    for rand in range(0,len(list3)):
        if len(str(list3[rand]%100)) < 2 :
            Schedule = str(int(list3[rand]/100)) +":"+str(list3[rand]%100)+str(0)
        else :  
            Schedule = str(int(list3[rand]/100)) +":"+ str(list3[rand]%100)
        list5.append(Schedule)
    if status==1:
        return {},list5

    else:
        return TimeTable,list5

# def TimeTableGenerator(input,*args,**kwargs): 
#     week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     weeks = list(week)
#     Period = {}

#     for i in Subjects.keys():
#         n = Subjects[i]
#         list1 = []
#         while n>0:
#             rand = random.randint(0,len(week)-1)
#             if Subjects[i]<len(week) and weeks[rand] in list1 :
#                 continue
#             list1.append(weeks[rand]) 
#             n-=1
#         Period[i] =  list1.copy()

#     Table={}
#     for i in weeks :
#         list2=[]
#         for j in Period.keys():
#             while i in Period[j] :
#                 list2.append(j)
#                 Period[j].remove(i)
#         Table[i]=list2.copy()

#     hi,mi = start.split(":")
#     ho,mo = end.split(":")
#     h,m = time.split(":")
#     hb,mb = time.split(":")

#     begin = int(hi+mi)
#     stop = int(ho+mo)
#     interval = int(h+m)
#     break2 = int(hb+mb)

#     list3 = [*range(begin,stop+1,interval+break2)]

#     TimeTable={}
#     status=0
#     for i in Table.keys():
#         Schedule={}
#         list4 = list3.copy()
#         if len(list3) < len(Table[i]):
#             status=1
#             break
#         for j in Table[i]:
#             rand = random.randint(0,len(list4)-1)
#             if len(str(list4[rand]%100)) < 2 :
#                 Schedule[j]= str(int(list4[rand]/100)) +":"+str(list4[rand]%100)+str(0)
#             else :  
#                 Schedule[j]= str(int(list4[rand]/100)) +":"+ str(list4[rand]%100)
#             list4.remove(list4[rand])

#             TimeTable[i] = dict(sorted(Schedule.items(), key = lambda x : int(x[1].split(":")[0] + x[1].split(":")[1]) ))

#     if status==1:
#         return {}

#     else :
#         return TimeTable,list3 
