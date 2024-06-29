from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return HttpResponse("""<html><head><title>Hello</title></head><body>Helo</body></html>""")