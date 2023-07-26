from django.shortcuts import render
from django.forms import *
from django.http import HttpResponse
# Create your views here.

def student(request):
    SO=Student_Form()
    
