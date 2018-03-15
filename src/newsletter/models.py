from django.db import models


class NewsLetter(models.Model):
	newsletter_email = models.EmailField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self): 
		return self.newsletter_email