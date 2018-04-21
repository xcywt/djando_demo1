from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

# Create your views here.
def index(request):
	context = {'messages':models.get_data()}	
	return render(request,'online/index.html', context)

def create(request):
	return render(request,'online/create.html')

def save(request):
	username = request.GET.get('username')
	title = request.GET.get('title')
	content = request.GET.get('content')
	#test = request.GET.get('xcytest')
	#print('test=' + test)
	models.save_data(username, title, content)
	return HttpResponseRedirect('/online/')
