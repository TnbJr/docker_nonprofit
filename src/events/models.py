from django.db import models

# Create your models here.

class Event(models.Model):
	event = models.CharField(max_length=255)
	description = models.TextField()
	location = models.CharField(max_length=255)
	event_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.event