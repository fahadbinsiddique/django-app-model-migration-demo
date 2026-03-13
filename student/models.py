from django.db import models

# Create your models here.
class StundentInfoModel(models.Model):
    Student_Name= models.CharField(max_length=120)
    age = models.PositiveIntegerField()