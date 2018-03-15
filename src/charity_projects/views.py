from django.shortcuts import render
from django.views.generic import View
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .models import CharityProject

# Create your views here.

class CharityProjectIndexView(View):
	template = "charity_projects/project_index.html"
	def get(self, request):
		projects_list = CharityProject.objects.filter(draft=False)
		paginator = Paginator(projects_list, 6) # Show 25 contacts per page
		page = request.GET.get('page')
		try:
			projects = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			projects = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			projects = paginator.page(paginator.num_pages)
		context = {
			"projects": projects,
		}
		return render(request, self.template, context)


class CharityProjectDetailView(View):
	template = "charity_projects/project_detail.html"
	def get(self, request, slug):
		instance = get_object_or_404(CharityProject, slug=slug)
		share_string = quote_plus(instance.title)
		context = {
			"instance": instance,
			"slug": slug,
			"share_string": share_string
		}
		return render(request, self.template, context)