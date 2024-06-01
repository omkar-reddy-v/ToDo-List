from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class addtask(models.Model):
    task = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.uid} {self.task} {self.date} {self.time}'
    


class staff(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phoneno = models.BigIntegerField()
    gender = models.CharField( max_length=50)
    uid = models.OneToOneField(User ,on_delete = models.CASCADE)



    def __str__(self):
        return f'{self.fullname} {self.email} {self.phoneno} {self.gender} {self.uid}'