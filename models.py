from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateTimeField()
    ggirlnum=models.IntegerField()
    isDelete=models.BooleanField()

class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    snum=models.integerField()
    
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)

    sgrade=models.ForeignKey("Grades")

