from django.contrib import admin
from .models import CharityProject

# Register your models here.


class CharityProjectsAdmin(admin.ModelAdmin):
	model = CharityProject
	exclude = ["slug"]



admin.site.register(CharityProject, CharityProjectsAdmin)