from django.shortcuts import render
from django.template.loader import  get_template
from django.template import context, RequestContext

# Create your views here.
def registration(request):
	return render(request,'registration.html')

def login(request):
	return render(request,"login.html")	