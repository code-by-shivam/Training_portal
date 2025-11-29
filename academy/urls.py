from django.urls import path
from . import views


urlpatterns = [
    path('courses/',views.Courses, name='courses'),  
    path('trainers/',views.Trainers, name='trainers'),  
    path('students/',views.Students, name='students'),
    path('course/detail/<int:id>',views.course_detail,name="course_detail"),
    path('course/edit/<int:id>',views.course_edit,name="edit_course"),
    path('course/delete/<int:id>',views.course_delete,name="delete_course"),
    path('trainer/detail/<int:id>',views.trainer_detail,name="trainer_detail"),
    path('trainer/edit/<int:id>',views.trainer_edit,name="trainer_edit"),
    path('trainer/delete/<int:id>',views.trainer_delete,name="trainer_delete"),
    path('student/detail/<int:id>',views.student_detail,name="student_detail"),
    path('student/edit/<int:id>',views.student_edit,name="student_edit"),
    path('student/delete/<int:id>',views.student_delete,name="student_delete"),
    path('student/add',views.student_add,name='student_add'),
    path('trainer/add',views.trainer_add,name="trainer_add"),
    path('course/add',views.course_add,name="course_add"),
]