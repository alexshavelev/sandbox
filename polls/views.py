from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hi, underdog. you're at polls index")
