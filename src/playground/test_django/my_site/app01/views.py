from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("hello world")

def index(request):
    return render(request, 'index.html')
