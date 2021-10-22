from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from enrollment.models import Student
# Create your views here.
def index(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'student_list':student})

def add_student(request, id=None):
    if(id != None):
        student = Student.objects.get(id=id)
        print(student)
    else:
        student = []
    return render(request, 'add-student.html', {'student_detail':student})

def student_profile(request, id=None):
    if(id != None):
        student = Student.objects.get(id=id)
        print(student)
    else:
        student = []
    return render(request,'studentProfilePopup.html', {'student_detail': student})

class create_student(APIView):
    "this method is used for create student"
    def post(self, request):
        data = request.data
        
        if 'student_name' in data and data['student_name'] != '':
            student_name = data['student_name']
        else:
            return Response({"message":'Name should not be blank.', 'error':1})
        
        father_name = data['father_name']
        
        if 'dob' in data and data['dob'] != '':
            dob = data['dob']
        else:
            return Response({"message":'DOB should not be blank.', 'error':1})
            
        if 'address' in data and data['address'] != '':
            address = data['address']
        else:
            return Response({"message":'Address should not be blank.', 'error':1})

        if 'phone_number' in data and data['phone_number'] != '':
            phone = data['phone_number']
        else:
            return Response({"message":'Phone number should not be blank.', 'error':1})
        
        city = data['city']
        state = data['state']
        pin = data['pin']

        if 'email_address' in data and data['email_address'] != '':
            email = data['email_address']
        else:
            return Response({"message":'Email address should not be blank.', 'error':1})
        class_opted = data['class_opted']
        marks = data['marks']
        date_enrolled = data['date_enrolled']
        if 'student_id' in data and data['student_id'] != '':
            student = Student.objects.get(id=data['student_id'])
        else:
            student = Student()
        student.student_name = student_name
        student.father_name = father_name
        student.dob = dob
        student.address = address
        student.city = city
        student.state = state
        student.pin = pin
        student.phoneNo = phone
        student.email = email
        student.class_opted = class_opted
        student.marks = marks
        student.date_enrolled = date_enrolled
        student.save()
        student_id = student.id
        if(student_id):
            return Response({"message":'Student added successfully', 'error':0})
        else:
            return Response({"message":'Student not added', 'error':1})
        