from django.shortcuts import render
from academy.models import Course, Trainer, Student

def Home(request):
    course = Course.objects.all()
    trainer = Trainer.objects.all()
    student = Student.objects.all()
    context = {'Courses': course, 'Trainers': trainer, 'Students': student}
    return render(request, 'home.html', context)