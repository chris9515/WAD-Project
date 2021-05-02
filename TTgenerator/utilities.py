from django.contrib.auth.models import User
from .models import Teacher, Student
import random, json


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

def TimeTableGenerator(input,*args,**kwargs):
    week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    weeks = list(week)
    Period = {}
    start = input['start']
    end = input['end']
    break1 = input['break1']
    time = input['time']
    Subjects = input['Subjects']

    for i in Subjects.keys():
        n = Subjects[i]
        list1 = []
        while n>0:
            rand = random.randint(0,len(week)-1)
            if Subjects[i]<len(week) and weeks[rand] in list1 :
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

    hi,mi = start.split(":")
    ho,mo = end.split(":")
    h,m = time.split(":")
    hb,mb = time.split(":")

    begin = int(hi+mi)
    stop = int(ho+mo)
    interval = int(h+m)
    break2 = int(hb+mb)

    list3 = [*range(begin,stop+1,interval+break2)]

    TimeTable={}
    status=0
    for i in Table.keys():
        Schedule={}
        list4 = list3.copy()
        if len(list3) < len(Table[i]):
            status=1
            break
        for j in Table[i]:
            rand = random.randint(0,len(list4)-1)
            if len(str(list4[rand]%100)) < 2 :
                Schedule[j]= str(int(list4[rand]/100)) +":"+str(list4[rand]%100)+str(0)
            else :  
                Schedule[j]= str(int(list4[rand]/100)) +":"+ str(list4[rand]%100)
            list4.remove(list4[rand])

            TimeTable[i] = dict(sorted(Schedule.items(), key = lambda x : int(x[1].split(":")[0] + x[1].split(":")[1]) ))

    if status==1:
        return {}

    else :
        return TimeTable,list3 
