from django.shortcuts import render

def render_home(request):
	return render(request, 'home.html')

def render_resume(request):
	pass

def render_projects(request):
	pass