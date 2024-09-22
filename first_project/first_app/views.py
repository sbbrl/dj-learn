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
    # return HttpResponse(f"""<html><head><title>Hello</title></head><body></body></html>""")
    tv_shows_list={"tv_shows":{'Game of Thrones':'9.3','Blacklist': '8','Suits': '8.5','The Witcher': '8.5','Test':None}}
    return render(request,'first_app/index.html',context=tv_shows_list)

def home(request):
    return HttpResponse("Welcome to home page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")
# def show_age(request,age):
#     return HttpResponse(f"I am {age} years old.")

def eod(request, num):
    if(num%2==0):
        output="%s is an even number." % num
    else:
        output="%s is an odd number." % num
    return HttpResponse(output)

def hello(request,name):
    return HttpResponse(f'Hello {name.split(" ")[0]} {name.split(" ")[1]}')