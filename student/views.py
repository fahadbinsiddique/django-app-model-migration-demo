from django.shortcuts import render
from student.models import *

def Read_Data(request):
    data=Student_Modal.objects.all()
    Data_Pack={
        "item": data
    }
    return render(request,"display.html",Data_Pack)

def Employee_Data(request):
    data=Student_Modal.objects.all()
    Data_Pack={
        "item": data
    }
    return render(request,"display.html",Data_Pack)