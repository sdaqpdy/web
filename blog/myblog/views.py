from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request ,'myblog/index.html',{'test':"My first page!!!!"})
# Create your views here.
