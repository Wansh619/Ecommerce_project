from django.contrib import admin
from .models import Phone, Otp,Purchased_item
# Register your models here.

# the information abut each model is in models.py
# here we are registering all our models in django databases
# for this firt we make migration  and the migratein django manage.py

admin.site.register(Phone)

admin.site.register(Otp)

admin.site.register(Purchased_item)
