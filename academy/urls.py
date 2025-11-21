from django.urls import path
from . import views


urlpatterns = [
    path('academy/courses/',views.Courses, name='courses'),  
    path('academy/trainers/',views.Trainers, name='trainers'),  
    path('academy/students/',views.Students, name='students'),
]