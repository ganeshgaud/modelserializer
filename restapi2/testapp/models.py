from django.db import models

# Create your models here.
class Student(models.Model):
    srno=models.IntegerField()
    sname=models.CharField(max_length=64)
    saddr=models.CharField(max_length=64)
    smarks=models.IntegerField()

    def __str__(self):
        return self.sname
