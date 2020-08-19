from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=20)
    sadd=models.CharField(max_length=50)
    scontact=models.IntegerField()
