from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Contact

def render_home(request):
	return render(request, 'home.html')

def render_resume(request):
	return render(request, 'resume.html')

def render_projects(request):
	return render(request, 'projects.html')

def render_contact(request):
	return render(request, 'contact.html')

def send_message(request):
	if request.method == "POST":
		errors = Contact.objects.contact_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value, extra_tags="contact")
		else:
			m = Contact.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], message=request.POST['message'])
			send_mail(subject='Portfolio Message', message=m.message, from_email=m.email, recipient_list=['kyle.logan.barnett@gmail.com'], fail_silently=True)
			messages.success(request, 'Message Sent')
	return redirect('/contact-me')

def download_resume(request):
	fs = FileSystemStorage()
	filename = 'kyle/static/Kyle_Barnett_Resume.pdf'
	response = HttpResponse(fs.open(filename), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Kyle_Barnett_Resume.pdf"'
	return response