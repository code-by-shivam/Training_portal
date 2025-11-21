from django.contrib import admin
from .models import Course, Trainer, Student
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','description','duration','course_image']
    list_filter = ['duration','course_name']
    search_fields = ['course_name','description']
    list_editable = ['duration','course_image']
    list_display_links = ['course_name','description']
    ordering = ['duration']
admin.site.register(Course, CourseAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id','full_Name','email','expertise','trainer_picture']
    list_filter = ['expertise','first_name']   # not use full_Name here as it is a method
    search_fields = ['full_Name','email','expertise']
    list_editable = ['expertise','trainer_picture',]    # Not use full_Name here as it is a method
    list_display_links = ['id','email','full_Name']
admin.site.register(Trainer, TrainerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','is_active','enrolled_courses','trainer']
    list_filter = ['is_active','enrolled_courses','trainer']
    search_fields = ['full_name','email','enrolled_courses','trainer']
    list_editable = ['is_active','enrolled_courses','trainer']
    list_display_links = ['id','email','full_name']

admin.site.register(Student, StudentAdmin)
