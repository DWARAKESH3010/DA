from django.db import models

# Create your models here.
class Datas(models.Model):
    Name = models.CharField(max_length=20,default="")
    Age = models.IntegerField(default=0)
    Address = models.CharField(max_length=50,default="")
    Contact = models.IntegerField(default=0)
    Email = models.CharField(max_length=20,default="")
