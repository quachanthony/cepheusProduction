from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def position(request):
    return render(request, 'position.html')

def details(request):
    return render(request, 'details.html')
