from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'main_menu/index.html')

def relative(request):
	return render(request,'main_menu/relative_url.html')

def CV(request):
	return render(request,'main_menu/CV.html')

def projects(request):
	return render(request,'main_menu/projects.html')
