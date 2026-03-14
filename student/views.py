from django.shortcuts import render
from student.models import *
# from student.template import *

# Create your views here.

def Read_Data(request):
    data=Student_Modal.objects.all()
    Data_Pack={
        "item": data
    }
    return render(request,"display.html",Data_Pack)