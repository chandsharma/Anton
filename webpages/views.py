from django.shortcuts import render
from django.template import RequestContext

def homepage(request):
    return render(request,'index.html')