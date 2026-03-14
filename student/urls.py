
from django.urls import path
from student.views import Read_Data

urlpatterns = [
    path('',Read_Data,name="Read_Data" ),
]
