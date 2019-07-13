from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<img src='https://www.w3schools.com/w3css/img_lights.jpg'>")