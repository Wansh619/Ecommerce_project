from django.shortcuts import render,redirect
from .models import  Phone ,Otp, Purchased_item
from django.contrib.auth.models import User ,auth
from django.contrib.auth import logout

from django.contrib import messages



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



# the otp entered by the user is equated the if there exist a model whose otp is same as otp of the user
# entered and if otp matches then user gets registered


# this is our login function 
# the functon first equate the password and email entered by user and if correct the user is authenticated 
# else get redirected to this page






# this is our logout function  for logging out


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



