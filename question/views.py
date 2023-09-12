from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    print("git_test")
    return HttpResponse('hello_world')
