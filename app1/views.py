from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<i><h2>This is belongs to app1 of firstview</h2></i>')