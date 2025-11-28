from django.shortcuts import render,get_object_or_404
from .models import Course, Trainer, Student
# Create your views here.

def Courses(request):
    courses = Course.objects.all()
    context = {'Courses': courses}
    return render(request, 'courses.html', context)

def Trainers(request):
    trainer= Trainer.objects.all()
    context = {'Trainers': trainer}
    return render(request, 'trainers.html', context)

def Students(request):
    student = Student.objects.all()
    context = {'Students': student}
    return render(request, 'students.html', context)

def course_detail(request,id):
    course = get_object_or_404(Course,id=id)
    context = {
        'course':course
    }
    return render(request,'course_detail.html',context)
    