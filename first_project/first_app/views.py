from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """        
    return HttpResponse(f"""<html><head><title>Hello</title></head><body></body></html>""")

def home(request):
    return HttpResponse("Welcome to home page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")
# def show_age(request,age):
#     return HttpResponse(f"I am {age} years old.")

# def even_or_odd(request, num):
#     if(num%2==0):
#         output="%s is an even number." % num
#     else:
#         output="%s is an odd number." % num
#     return HttpResponse(output)

def hello(request,name):
    return HttpResponse(f'Hello {name.split(" ")[0]} {name.split(" ")[1]}')