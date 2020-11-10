from django.db import models

# Create your models here.
class Student(models.Model):
    No= models.IntegerField()
    Name = models.CharField(max_length=25)
    Age = models.IntegerField()
    Mob = models.IntegerField()
    Add = models.CharField(max_length=64)


