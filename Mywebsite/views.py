from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Mywebsite/addnews.html')

def addnews(request):
    return render(request,'Mywebsite/addnews.html')

def result(request):
    name = request.GET['name_news']
    detial = request.GET['name_detail']
    mydata = {
        'name_news':name,
        'name_detail':detial
    }
    return render(request,'Mywebsite/result.html',mydata)