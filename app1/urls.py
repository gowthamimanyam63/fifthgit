from django.urls import path
from app1.views import *
app1_name='anything1'
urlpatterns=[
    path('first/',first,name='first'),
]