from django.shortcuts import render,redirect
from .models import  Phone ,Otp, Purchased_item
from django.contrib.auth.models import User ,auth
from django.contrib.auth import logout

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
   



# this is our main homepage for displaying all the products and is the first page of our website
# Phones collect all the list of object from our Phone database indjango admin and sending it to our index.html

def index(request):
    Phones=Phone.objects.all()
    return render(request,'index.html',{'Phones':Phones})





# this is our registration funtion for users for registering their account  to website
#  1 it take username ,email id ,passwoed as input
#  2 if user exist or detail is missing then it returns to the same page with repective message get reflected
#  3 if all things satify the we procede to otp generation
#  4 here our otp variable generate random number in form of string and the otp with user details is stroed in our OTP model in django admin database
#  5 As well as email is also send to user on their email using send_otp function
#  6 Then we further procede to our otp_verf webpage

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

# the otp entered by the user is equated the if there exist a model whose otp is same as otp of the user
# entered and if otp matches then user gets registered

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

# this is our login function 
# the functon first equate the password and email entered by user and if correct the user is authenticated 
# else get redirected to this page


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



# this is our logout function  for logging out
def log_out(request):
    logout(request)
    return redirect('index')


# responsible for Showing all order registory in order .html

def order(request):
    item=Purchased_item.objects.all()
    return render(request,'order.html',{'Purchased_item':item})




# this function is for registering the order of user in the the purchased  database

def buy(request,p):
        if request.user.is_authenticated:
            if request.method =='POST':
                 quantity=request.POST['quantity']
                 Address=request.POST['address']
                 phone=Phone.objects.get(name=p)
                 name=phone.name
                 order=Purchased_item.objects.create(productname=name,quantity=quantity,Address=Address)
                 order.save()
                 messages.info(request,"order placed")
                 return redirect('index')
            else:
             phone=Phone.objects.get(name=p)
             return render(request,'buy.html',{'phone':phone})
        else:
           return redirect('login')



