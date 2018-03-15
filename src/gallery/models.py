from django.db import models

# Create your models here.


class Gallery(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField()
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_image_url(self):
		return self.image.url

	# class Meta:
	# 	ordering = ['-created']