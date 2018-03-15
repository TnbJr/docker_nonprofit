from django import forms
from .models import Donation

class DonateForm(forms.ModelForm):
	
	class Meta:
		model = Donation
		fields = [ 'first_name', 'last_name', 'donate_email', 'donation_amount', 'donation_comment']

	def __init__(self, *args, **kwargs):
		super(DonateForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['donate_email'].widget.attrs['placeholder'] = 'youremail@email.com'
		self.fields['donation_amount'].widget.attrs['min'] = 0