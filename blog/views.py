from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse('<h1>Blog Home</h1>')

def aboutPage(request):
    return HttpResponse('<h1>Blog About</h1>')

