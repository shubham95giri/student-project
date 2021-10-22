from django.contrib import admin
from django.urls import path
from enrollment import views

urlpatterns = [
    path("", views.index, name= 'enrollment'),
    path("add-student", views.add_student, name='addstudent'),
    path("add-student/<id>", views.add_student, name='addstudent'),
    path("createstudent", views.create_student.as_view()),
    path("student-profile/<id>", views.student_profile, name='studentProfile')
]
