from django.db import models

# Create your models here.

class Student(models.Model):
    studentNumber = models.PositiveIntegerField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    studyField = models.CharField(max_length=50)
    gpa = models.FloatField()
    def __str__(self):
        return f' Student {self.firstName} {self.lastName}'