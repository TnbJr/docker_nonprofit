from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from contact.forms import ContactForm
from newsletter.forms import NewsLetterForm
from charity_projects.models import CharityProject
from events.models import Event

# Create your views here.
class IndexView(View):	
	template = 'index.html'
	def get(self, request):
		events = Event.objects.filter(draft=False, event_date__gte=timezone.now())[:4]
		projects = CharityProject.objects.filter(draft=False, featured=True)[:4]
		context = {
			"newsletter_form": NewsLetterForm,
			"form": ContactForm,
			"projects": projects,
			"events": events	
		}
		return render(request, self.template, context)


class AboutView(View):
	template = 'about.html'
	def get(self, request):
		context = {
		}
		return render(request, self.template, context)


class ShareView(View):
	template = 'share.html'
	def get(self, request):
		return render(request, self.template)