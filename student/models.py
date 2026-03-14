from django.db import models

# Create your models here.
class Student_Modal(models.Model):
    name    = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile  = models.CharField(max_length=15)
    nid     = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Employee_Modal(models.Model):
    name    = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile  = models.CharField(max_length=15)
    designation = models.CharField(max_length=20)
    