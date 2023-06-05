import email
import random
from telnetlib import LOGOUT
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib import auth
from mycar.models import Contact
from django.contrib import messages #For displaying message alert
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Car
from .models import Test_Drive
from django.utils.translation import gettext
from django.contrib.auth import get_user_model
from django.conf.urls.static import static 
from django.contrib.auth.hashers import make_password, check_password
import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors
User = get_user_model() 

# Create your views here.
def index(request):
    cars=Car.objects.all()
    print(cars)
    params={'car':cars}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contactus=Contact(name=name,email=email,phone=phone,desc=desc) #creating object of contact
        contactus.save() #saving all the info
        messages.success(request, 'Your form has been sent successfully!')
    return render(request,'contactus.html')
def loginuser(request):
    user=None
    if request.method=="POST":
        Username1=request.POST["username1"]
        Password1=request.POST["password1"]
        user = authenticate(username=Username1,password=Password1)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in!")
            return redirect("/home")       
        else:
            messages.warning(request, 'Sorry! You have entered invalid credentials')
            return redirect("/loginuser")
    return render(request,'loginuser.html')
def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully Logged Out!')
    return render(request,'logoutuser.html')
def registeruser(request):
    if request.method=="POST":
        fname=request.POST['fname']
        username=request.POST['your_email']
        password=request.POST['password']
        cnf_pass=request.POST['cnf_pass']
        if(password!=cnf_pass):
            messages.warning(request,"Passwords do not match!")
            return redirect('/registeruser')
        if(len(password)<8):
            messages.warning(request,"Password too short!")
            return redirect('/registeruser')
        myuser = User.objects.create_user(username,password)
        myuser.first_name=fname
        myuser.email=username
        myuser.username=username
        myuser.set_password(password)
        myuser.save()
        messages.success(request,"Your Profile has been successfully created!")
        return redirect('/loginuser')
    return render(request,'registeruser.html')
def checkout(request):
    id=random.randint(100000,1000000)
    cars=Car.objects.all()
    params={'car':cars,'id':id}
    return render(request,'checkout.html',params)
def test_drive(request):
    if request.method=="POST":
        cust1_name=request.POST.get('cust1_name')
        cust1_email=request.POST.get('cust1_email')
        cust1_phone=request.POST.get('cust1_phone')
        car_name=request.POST.get('car_name')
        choose_date=request.POST.get('choose_date')
        booking_order=test_drive(cust1_name=cust1_name,cust1_email=cust1_email,cust1_phone=cust1_phone,car_name=car_name,choose_date=choose_date)
        booking_order.save()
        messages.success(request, 'Test Drive Booked Successfully!')
    return render(request,'test_drive.html')
def show_cars(request):
    cars=Car.objects.all()
    print(cars)
    n=len(cars)
    params={'no_of_slides':n,'range':range(1,n),'car':cars}
    return render(request,'show_cars.html',params)
def search(request):
    query=request.GET['query']
    allcars=Car.objects.filter(Model__icontains=query)
    cars=Car.objects.all()
    n=len(allcars)
    params={'slides':n,'allcars':allcars,'range':range(0,n),'car':cars}
    return render(request,'search.html',params)

def getdata(price,dis,cyl,driv,emm,fuel,body,doors,gears,seating,type1,abs):
    model=pickle.load(open('static\CarBlink3.py','rb'))
    X=[[price,dis,cyl,driv,emm,fuel,body,doors,gears,seating,type1,abs]]
    distances,indices=model.kneighbors(X)
    return indices

def result(request):
    price=int(request.POST.get('price',0))
    dis=int(request.POST.get('dis',0))
    cyl=int(request.POST.get('cyl',0))
    driv=int(request.POST.get('driv',0))
    emm=int(request.POST.get('emm',0))
    fuel=int(request.POST.get('fuel',0))
    body=int(request.POST.get('body',0))
    doors=int(request.POST.get('doors',0))
    gears=int(request.POST.get('gears',0))
    seating=int(request.POST.get('seating',0))
    type1=int(request.POST.get('type1',0))
    abs=int(request.POST.get('abs',0))
    result=getdata(price,dis,cyl,driv,emm,fuel,body,doors,gears,seating,type1,abs)
    cars=Car.objects.all()
    params={'car':cars,'result':result}
    return render(request,'result.html',params)

def findcar(request):
    return render(request,'findcar.html')

def calc(request):
     return render(request,'calc.html')