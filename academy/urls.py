from django.urls import path
from . import views


urlpatterns = [
    path('courses/',views.Courses, name='courses'),  
    path('trainers/',views.Trainers, name='trainers'),  
    path('students/',views.Students, name='students'),
    path('courses/<int:id>',views.course_detail,name="course_detail")

]