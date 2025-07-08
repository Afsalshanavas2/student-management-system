from django.db import models

# Create your models here.

class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=100)
    stud_class = models.CharField(max_length=50)
    stud_division = models.CharField(max_length=50)
    stud_gender = models.CharField(max_length=10)
    stud_contact = models.CharField(max_length=15)
    stud_place = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.stud_id} - {self.stud_name}"