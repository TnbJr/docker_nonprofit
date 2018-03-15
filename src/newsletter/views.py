from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .forms import NewsLetterForm
from .models import NewsLetter


class NewsLetterView(View):
	form = NewsLetterForm

	def post(self, request):
		form = self.form(request.POST or None)
		if form.is_valid():
			print("form is valid")
			email = form.cleaned_data.get("email")
			data = {
				"email": email
			}
			instance = form.save(commit=False)
			instance.save()
			return JsonResponse(data)
		data = {
			"form_errors": form.errors.as_json()
		}
		print(form.errors.as_json())
		return JsonResponse(data, status=400)