from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import ContactForm
from crispy_forms.utils import render_crispy_form
from django.core.context_processors import csrf 

class ContactView(View):
	form = ContactForm
	template = "contact/contact.html"

	def get(self, request):
		context = {
			"form": self.form
		}
		return render(request, self.template, context)


	def post(self, request):
		form = self.form(request.POST or None)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER]
			send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
			form.save()
			return JsonResponse({'success': True})
		captcha_key = CaptchaStore.generate_key()
		captcha_img = captcha_image_url(captcha_key)
		data = {
			"form_errors": form.errors.as_json(),
			"key": captcha_key,
			"img_url": captcha_img
		}
		return JsonResponse(data, status=400)