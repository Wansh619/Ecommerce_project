from django.urls import path
from . import views

# these are all the urls added for our webpage
urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('otp',views.otp_verf,name='otp'),
    path('logout',views.log_out,name='logout')
]