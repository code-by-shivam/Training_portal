from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in weeks")
    course_image = models.ImageField(upload_to = 'Course/')

    def __str__(self):
        return f"{self.course_name}"


class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, help_text="Python, Django, Data Science")
    trainer_picture = models.ImageField(upload_to = 'Trainer/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_Name(self):
        return f"{self.first_name} {self.last_name}"



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_courses = models.ForeignKey(Course, on_delete = models.SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete = models.SET_NULL, null=True, blank=True)
    

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    