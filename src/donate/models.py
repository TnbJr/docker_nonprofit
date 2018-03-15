from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings

# Create your models here.


class Donation(models.Model):
	first_name = models.CharField(max_length=120, blank=True, null=True)
	last_name = models.CharField(max_length=120, blank=True, null=True)
	donate_email = models.EmailField()
	donation_amount = models.DecimalField(decimal_places=2, max_digits=20)
	donation_comment = models.TextField(blank=True, null=True)
	


	def __str__(self): 
		return "{0} {1}-${2}".format(self.first_name, self.last_name, self.donation_amount)