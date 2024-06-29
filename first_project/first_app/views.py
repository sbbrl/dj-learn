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