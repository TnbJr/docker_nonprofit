from django import forms
from .models import NewsLetter

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = NewsLetter
		fields = ['newsletter_email']
	
	newsletter_email = forms.EmailField(
        label='Email', 
        widget=forms.TextInput(
            attrs={ 'placeholder': 'Enter your email here...'}
        )
    )
