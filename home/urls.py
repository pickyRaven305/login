from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index,name = 'home'),
    path('login', views.loginUser,name = 'login'),
    path('logout', views.logoutUser,name = 'logout'),
    path('feedback', views.feedback,name = 'feedback'),
    path('studReg', views.studentRegisteration,name = 'Student Registeration'),
    path('staffReg', views.staffRegisteration,name = 'staff Registeration'),
    path('courseReg', views.courseRegisteration,name = 'Course Registeration'),
    path('subReg', views.subjectRegisteration,name = 'subject Registeration'),
    
    
    #path('attendence', views.attendence,name = 'attendence'),
    
    
]