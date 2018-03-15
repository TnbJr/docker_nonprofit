from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify 
# Create your models here.

class CharityProject(models.Model):
	title = models.CharField(max_length=255, unique=True)
	slug = models.SlugField()
	image = models.ImageField()
	content = models.TextField()
	draft = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	featured = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse("project:detail", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			super().save(*args, **kwargs)
		else:
			super().save(*args, **kwargs)

	def get_image_url(self):
		return self.image.url

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']
