import email
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField, EmailField, IntegerField
from django.contrib.auth.models import User

class Contact(models.Model): # So let,s understand what is happening here.So when a person visits on your site and filled the contact us form and submit it then you need that user details which he filled in the form so for this task you have to create models. In this model class "contact" mean a table name called contact is created and it,s column names are "name ","email","phone".But after doing all this you need to apply migration but before applying migrations you need to register your model in admin.py file.Basically migration create a file which stores all the changes defined in your model.After all this run migrate command which actual creates that table named "contact"
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=120)
    phone=models.IntegerField()
    desc=models.CharField(max_length=300)
    
    def __str__(self): #this function we used for save details by name in database
        return self.name
class Car(models.Model):
    Make=models.CharField(max_length=100)
    Model=models.CharField(max_length=100)
    Variant=models.CharField(max_length=100)
    Price=models.IntegerField()
    Displacement=models.IntegerField()
    Cylinder=models.IntegerField()
    Drivetrain=models.CharField(max_length=50)
    Emission=models.CharField(max_length=50)
    Fueltype=models.CharField(max_length=50)
    Bodytype=models.CharField(max_length=50)
    Doors=models.IntegerField()
    Gears=models.IntegerField()
    Seating_capacity=models.IntegerField()
    Type=models.CharField(max_length=50)
    ABS=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',default="")

    def __str__(self): #this function we used for save details by name in databas
        return self.Model
class Test_Drive(models.Model):
    cust1_name=models.CharField(max_length=100)
    cust1_email=models.EmailField(max_length=120)
    cust1_phone=models.IntegerField(blank=True,null=True)
    car_name=models.CharField(max_length=100)  
    choose_date=models.DateField()

    def __str__(self):
        return self.cust1_name
    

