from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = ' <html> <body> Hello django. </body> </html>'
    return HttpResponse(html)

def welcome(request):
    html = '<html> <body> <h1>Welcome to Django. </h1> </body> </html>'
    return HttpResponse(html)  

def test_template(request):
    return render(request, 'test.html')