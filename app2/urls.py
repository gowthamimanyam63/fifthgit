from django.urls import path
from app2.views import *
app2_name='anything2'
urlpatterns=[
    path('second/',second,name='second'),
]