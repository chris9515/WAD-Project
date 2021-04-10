from django.urls import path
from .views import TimeTableGenerator, InstituteUse, StudentRegister, FacultyRegister, StudentLogin, FacultyLogin, studentProfileView, teacherProfileView, logoutView, PersonnalUse

urlpatterns = [
    path('TTGenerator', TimeTableGenerator, name = 'TTGenerator'),
    path('InstituteUse', InstituteUse, name='InstituteUse'),
    path('PersonnalUse', PersonnalUse, name='PersonnalUse'),
    path('studentSignUp', StudentRegister, name='studentSignUp'),
    path('facultySignUp', FacultyRegister, name='facultySignUp'),
    path('studentLogin', StudentLogin, name='studentLogin'),
    path('facultyLogin', FacultyLogin, name='facultyLogin'),
    path('teacherProfile', teacherProfileView, name="teacherProfile"),
    path('studentProfile', studentProfileView, name="studentProfile"),
    path('logout', logoutView, name="logout"),
]