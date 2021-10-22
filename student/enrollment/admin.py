from django.contrib import admin
from enrollment.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'father_name', 'dob', 'address', 'city', 'phoneNo', 'email', 'marks', 'class_opted')

# Register your models here.
admin.site.register(Student, StudentAdmin)