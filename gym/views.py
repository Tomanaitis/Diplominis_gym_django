from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("GYM IS ABOUT TO BE OPEN!!!")
