from django.db import models

# Create your models here.

class Student(models.Model):

    student_name= models.TextField(null = True, blank= True)
    father_name= models.TextField(null = True, blank= True)
    dob= models.DateTimeField(null = True, blank= True)
    address= models.TextField(null = True, blank= True)
    city = models.TextField(null = True, blank= True)
    state = models.TextField(null = True, blank= True)
    pin = models.TextField(null = True, blank= True)
    phoneNo = models.TextField(null = True, blank= True)
    email = models.TextField(null = True, blank= True)
    class_opted = models.TextField(null = True, blank= True)
    marks = models.TextField(null = True, blank= True)
    date_enrolled = models.DateTimeField(null = True, blank= True)
    date_added= models.DateTimeField(auto_now= True)
    
    class Meta:
        db_table = 'Student'

