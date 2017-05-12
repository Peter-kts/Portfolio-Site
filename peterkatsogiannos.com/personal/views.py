from django.shortcuts import render


def index(request):
	return render(request, 'personal/index.html')

def about(request):
	return render(request, 'personal/about.html')

def projects(request):
	return render(request, 'personal/projects.html')

def willwalt(request):
	return render(request, 'personal/willwalt.html')

def arcadebot(request):
	return render(request, 'personal/arcadebot.html')
	
# Create your views here.
