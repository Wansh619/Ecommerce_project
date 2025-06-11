from django.urls import path
from . import views
urlpatterns=[
    path('log_in',views.index,name='index')
    
]