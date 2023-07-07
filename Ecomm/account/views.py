from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import logout
from buy.models import Otp
from django.contrib import messages


# for sending email 
import smtplib as sm

# this is for generating random otp for registration
import random


# this is the email id and the password which we will be using for our website to generate otp via email 
# NOTE-> the email could be a spam  So check for email in spam section to verify otp

PASSWORD='ijrrgrwxzaqwnbgw'
EMAIL='unitycreator619@gmail.com'

# initialising our gmal server at the respective port for sending verificcation emails
# at first we are starting our server and then logging in using EMAIL and PASSWORD

SERVER= sm.SMTP('smtp.gmail.com',587)
SERVER.starttls()

SERVER.login(EMAIL,PASSWORD)

# This is the defalt message layout for our email sending 

MSG='HEre is your one time password for Creating your account on our website '




# this function is responsible for sending otp to respective email in argument

def send_otp(email,otp):
    SERVER.sendmail(EMAIL,email,MSG+otp)
   


# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if email or username or password is None :
            messages.info(request,"PLESE ENTER THE REQUIRED DETAILS")
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.info(request,"USER WITH SAME PHONE NO EXIST")
            return redirect('register')
        else:
            otp=str(random.randint(1000,9999))
            send_otp(email,otp)
            OTP =Otp.objects.create(otp=otp,email=email,password=password,username=username)
            OTP.save()
            return render(request,'otp.html')
    else:
        return render(request,'register.html')
    

def otp_verf(request):
    if request.method =='POST':
        otp=request.POST['otp']
        check=Otp.objects.filter(otp=otp).exists()
        if  check:
            obj=Otp.objects.filter(otp=otp).get()
            user =User.objects.create_user( username=obj.username,email=obj.email,password=obj.password)
            user.save()
            Otp.objects.filter(otp=otp).delete()
            return render(request,'login.html')

        else:
            messages.info(request,"invalid OTP ")
            return render(request,'OTP.html')
    else:
        return render(request,'OTP.html')    
    
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('index')
        else:      
            messages.info(request,"wrong credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('index')