from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second(request):
    return HttpResponse('<h2><i>This view belong to app2 of second</i></h2>')