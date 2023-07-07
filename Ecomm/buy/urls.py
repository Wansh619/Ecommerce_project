from django.urls import path
from . import views

# these are all the urls added for our webpage
urlpatterns=[



path('',views.index, name='index'),
path('buy/<str:p>',views.buy,name='buy'),
# path('login',views.login,name='login'),
# path('register',views.register,name='register'),
# path('otp_verf',views.otp_verf,name='otp_verf'),
# path('logout',views.log_out,name='logout'),


# this is a secretely generatede webpage for the seeing the registered orders on their data
 path('order',views.order,name ='order')
]

