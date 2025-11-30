from django.shortcuts import render,get_object_or_404,redirect
from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm,StudentForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.


def Courses(request):
    courses = Course.objects.all()
    context = {'Courses': courses}
    return render(request, 'courses.html', context)


@permission_required('academy.view_trainer', raise_exception=True)
def Trainers(request):
    trainer= Trainer.objects.all()
    context = {'Trainers': trainer}
    return render(request, 'trainers.html', context)


@permission_required('academy.view_student', raise_exception=True)
def Students(request):
    student = Student.objects.all()
    context = {'Students': student}
    return render(request, 'students.html', context)


@permission_required('academy.view_course', raise_exception=True)
def course_detail(request,id):
    course = get_object_or_404(Course,id=id)
    context = {
        'course':course
    }
    return render(request,'course_detail.html',context)



@login_required
@permission_required('academy.change_course', raise_exception=True)
def course_edit(request,id):
    course = get_object_or_404(Course,id=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('courses')
    else:
        print(form.errors)
    context = {
        'form' : form,
        'course' : course
    }
    return render(request,"edit_course.html",context)

@login_required
@permission_required('academy.delete_course', raise_exception=True)
def course_delete(request,id):
    course = get_object_or_404(Course,id=id)
    course.delete()
    return redirect('courses')


@login_required
@permission_required('academy.view_trainer', raise_exception=True)
def trainer_detail(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    context = {
        'trainer':trainer
    }
    return render(request,'trainer_detail.html',context)

@login_required
@permission_required('academy.change_trainer', raise_exception=True)
def trainer_edit(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    form = TrainerForm(request.POST or None, instance=trainer)
    if form.is_valid():
        form.save()
        return redirect('trainers')
    else:
        print(form.errors)
    context = {
        'form' : form,
        'trainer' : trainer
    }
    return render(request,"edit_trainer.html",context)

@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def trainer_delete(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    trainer.delete()
    return redirect('trainers')  


@login_required
@permission_required('academy.view_student', raise_exception=True)
def student_detail(request,id):
    if request.user.groups.filter(name="Student").exists():
        return HttpResponseForbidden("Students cannot view other student's details.")
    student = get_object_or_404(Student,id=id)
    context = {
        'student':student
    }
    return render(request,'student_detail.html',context)


@login_required
@permission_required('academy.change_student', raise_exception=True)
def student_edit(request,id):
    student = get_object_or_404(Student,id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students')
    else:
        print(form.errors)
    context = {
        'form' : form,
        'student' : student
    }
    return render(request,"edit_student.html",context)



@login_required
@permission_required('academy.delete_student', raise_exception=True)
def student_delete(request,id):
    student = get_object_or_404(Student,id=id)
    student.delete()
    return redirect('students') 


@login_required
@permission_required('academy.add_student', raise_exception=True)
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students') 
        else:
            print(forms.errors)
    form = StudentForm()
    context = {
        'form':form
    }
    return render(request,"add_student.html",context)
    
@login_required
@permission_required('academy.add_trainer', raise_exception=True)
def trainer_add(request):
    if request.method == "POST":
        form = TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainers') 
        else:
            print(forms.errors)
    form = TrainerForm()
    context = {
        'form':form
    }
    return render(request,"add_trainer.html",context)

@login_required
@permission_required('academy.add_course', raise_exception=True)
def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses') 
        else:
            print(forms.errors)
    form = CourseForm()
    context = {
        'form':form
    }
    return render(request,"add_course.html",context)