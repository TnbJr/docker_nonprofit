from django.shortcuts import render
from django.views.generic import View
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Gallery
# Create your views here.


class GalleryView(View):
	def get(self, request):
		template = 'gallery/gallery.html'
		gallery = Gallery.objects.filter(draft=False)
		context = {
			"gallery": gallery,	
		}
		return render(request, template, context)