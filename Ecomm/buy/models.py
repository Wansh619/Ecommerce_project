from django.db import models
from datetime import datetime


# Create your models here.



# this is the model for all phones -> Every phone data tored in this model

class Phone(models.Model):
    imgurl=models.CharField(max_length=1000000000000000,default="")
    name= models.CharField(max_length=40)
    price=models.IntegerField()
    description= models.CharField(max_length=2000)
    RAM =models.IntegerField(default=4)
    Device_storage=models.IntegerField(default=64)
    OS=models.CharField(default="Android",max_length=10)
 
   


    def __str__(self):
        return self.name



# this is a model which store temprory otp information just for registering purposes the object gets deleted as soon as the user got registered in our website

class Otp(models.Model):
    otp=models.CharField(max_length=5,default='?')
    username=models.CharField(max_length=15,default='?')
    email=models.CharField(max_length=15,default='?')
    password=models.CharField(max_length=18,default='?')




# this model is for purchasing a product in our website which stores the data for the company of the product buyed by a user
class Purchased_item(models.Model):
    productname=models.CharField (max_length=70)
    Address=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    date= models.DateTimeField(default =datetime.now , blank=True)






