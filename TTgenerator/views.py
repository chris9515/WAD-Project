from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .utilities import processFacultyRegistrarionForm, schedulingalgo
from django.contrib import messages
from django.contrib.auth.models import User
import json
import random as rand


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
        # print(data)
        # week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        # subjects = request.POST.getlist('subject')
        # periods = request.POST.getlist('periods')
        # start_time = request.POST.get('startTime')
        # end_time = request.POST.get('endTime')
        # break_time = request.POST.get('breakTime')
        # duration = request.POST.get('breakDuration')
        # subject_data = dict()
        # for i in range(len(subjects)):  
        #     subject_data[subjects[i]] = periods[i]
        # print(subject_data)
        # output,times = schedulingalgo(start_time,end_time,break_time,duration,subject_data)
        # list2 = []
        # for i in range(len(times)-1):
        #     hi,mi =times[i].split(":")
        #     ho,mo = "1:00".split(":")
        #     hi = int(hi) 
        #     ho=int(ho)
        #     mi=int(mi) 
        #     mo=int(mo)
        #     h = hi+ho   
        #     m = mi+mo
        #     if m>60:
        #         h+=1
        #         m=m%60
        #     if len(str(m))<2 : 
        #         time1 = str(h)+":"+str(m)+'0'
        #     else:
        #         time1 = str(h)+":"+str(m)
        #     time = times[i] + '-'+ time1
        #     list2.append(time)
        # for i in output.keys():
        #     output[i] =dict([(value, key) for key, value in output[i].items()])
        # # print(output)
        # times.pop()
        # for i in output.keys():
        #     for j in times:
        #         if j in output[i].keys():
        #             continue
        #         else:
        #             output[i][j] = ' None'
        #     output[i]['12:00']='LUNCH'        
        # for i in output.keys():
        #     output[i] = dict(sorted(output[i].items(), key = lambda x : int(x[0].split(":")[0] + x[0].split(":")[1]) ))
        # dict(sorted(output.items()))
        # return render(request, 'TimetablePlanner.html', {'output' : output,'times':times,'list2':list2, 'week':week, 'subjects':subject_data})
        return render(request, 'TimeTablePlanner.html')
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

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.05

class Data:
    def __init__(self):
        self._rooms = Room.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses = Course.objects.all()
        self._depts = Department.objects.all()

    def get_rooms(self): 
        return self._rooms

    def get_instructors(self): 
        return self._instructors

    def get_courses(self): 
        return self._courses

    def get_depts(self): 
        return self._depts

    def get_meetingTimes(self): 
        return self._meetingTimes

class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): 
        return self._numberOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        sections = Section.objects.all()
        for section in sections:
            dept = section.department
            n = section.noClassesInWeek
            if n <= len(MeetingTime.objects.all()):
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.sectionID, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes()[rand.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(data.get_rooms()[rand.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(crs_inst[rand.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)
            else:
                n = len(MeetingTime.objects.all())
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept, section.sectionID, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes()[rand.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(data.get_rooms()[rand.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(crs_inst[rand.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)

        return self

    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            if classes[i].room.capacity < int(classes[i].course.maxStudents):
                self._numberOfConflicts += 1
            for j in range(len(classes)):
                if j >= i:
                    if (classes[i].meetingTime == classes[j].meetingTime) and \
                            (classes[i].sectionID != classes[j].sectionID) and (classes[i].section == classes[j].section):
                        if classes[i].room == classes[j].room:
                            self._numberOfConflicts += 1
                        if classes[i].instructor == classes[j].instructor:
                            self._numberOfConflicts += 1
        return 1 / (1.0 * self._numberOfConflicts + 1)

class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rand.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rand.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rand.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


class Class:
    def __init__(self, id, dept, section, course):
        self.sectionID = id
        self.department = dept
        self.course = course
        self.instructor = None
        self.meetingTime = None
        self.room = None
        self.section = section

    def get_id(self): 
        return self.sectionID

    def get_dept(self): 
        return self.department

    def get_course(self): 
        return self.course

    def get_instructor(self): 
        return self.instructor

    def get_meetingTime(self): 
        return self.meetingTime

    def get_room(self): 
        return self.room

    def set_instructor(self, instructor): 
        self.instructor = instructor

    def set_meetingTime(self, meetingTime): 
        self.meetingTime = meetingTime

    def set_room(self, room): 
        self.room = room


data = Data()


def context_manager(schedule):
    classes = schedule.get_classes()
    context = []
    cls = {}
    for i in range(len(classes)):
        cls["section"] = classes[i].sectionID
        cls['dept'] = classes[i].department.deptName
        cls['course'] = f'{classes[i].course.courseName} ({classes[i].course.courseID}, ' \
                        f'{classes[i].course.maxStudents}'
        cls['room'] = f'{classes[i].room.roomNo} ({classes[i].room.capacity})'
        cls['instructor'] = f'{classes[i].instructor.name} ({classes[i].instructor.instructorID})'
        cls['meeting_time'] = [classes[i].meetingTime.pid, classes[i].meetingTime.day, classes[i].meetingTime.time]
        context.append(cls)
    return context

def timetable(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()

    return render(request, 'timetable.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                              'times': MeetingTime.objects.all()})

def AddFaculty(request):
    form = InstructorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addFaculty')
    return render(request, 'AddFaculty.html', {'form':form})

def instructorView(request):
    context = {
        'instructors': Instructor.objects.all()
    }
    return render(request, 'InstituteList.html', context)

def deleteInstructor(request, pk):
    temp = Instructor.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editInstructor')

def addRoom(request):
    form = RoomForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addRoom')
    return render(request, 'AddRoom.html', {'form':form})

def roomList(request):
    context={
        'rooms': Room.objects.all()
    }
    return render(request, 'RoomList.html', context)

def deleteRoom(request, pk):
    temp = Room.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editRooms')

def meetingListView(request):
    context={
        'meetingTime':MeetingTime.objects.all()
    }
    return render(request, 'MeetingList.html', context)

def addMeetingTime(request):
    form = MeetingTimeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addMeetingTime')
        else:
            print('Invalid')
    return render(request, 'addMeeting.html', {'form':form})

def deleteMeetingTime(request, pk):
    temp = MeetingTime.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editMeetingTime')

def courseListView(request):
    context={
        'courses': Course.objects.all()
    }
    return render(request, 'CourseList.html', context)

def addCourse(request):
    form = CourseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addCourse')
    else :
        print("Invalid")
    return render(request, 'AddCourse.html', {'form':form})

def deleteCourse(request, pk):
    temp = Course.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editCourse')

def addDepartment(request):
    form = DepartmentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addDepartment')
    return render(request, 'AddDepartment.html', {'form':form})

def departmentList(request):
    context = {
        'departments': Department.objects.all()
    }
    return render(request, 'DepartmentList.html', context)

def deleteDepartment(request, pk):
    temp = Department.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editDepartment')

def addSection(request):
    form = SectionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addSection')
    return render(request, 'AddSection.html', {'form':form})

def sectionList(request):
    context = {
        'sections': Section.objects.all()
    }
    return render(request, 'SectionList.html', context)

def deleteSection(request, pk):
    temp = Section.objects.filter(pk=pk)
    if request.method == 'POST':
        temp.delete()
        return redirect('editSection')

