from django.db import models
import re

class ContactManager(models.Manager):
	def contact_validator(self, post_data):
		errors = {}
		email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(post_data['first_name']) < 2:
			errors['first_name'] = "First name must be at least 2 characters"
		if len(post_data['last_name']) < 2:
			errors['last_name'] = "Last name must be at least 2 characters"
		if not email_regex.match(post_data['email']):
			errors['email'] = "Invalid email address"
		if len(post_data['message']) < 10:
			errors['message'] = "Message must be at least 10 characters"
		return errors

class Contact(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ContactManager()
