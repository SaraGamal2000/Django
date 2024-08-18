from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def infotrack(request):
    return HttpResponse('<h1> hellow  info infotrack<h2>')