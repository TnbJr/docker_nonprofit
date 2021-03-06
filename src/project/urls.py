"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import IndexView, AboutView, ShareView

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^newsletter/', include('newsletter.urls', namespace='newsletter')),
	url(r'^contact/', include('contact.urls', namespace='contact')),
	url(r'^donate/', include('donate.urls', namespace='donate')),
	url(r'^gallery/', include('gallery.urls', namespace='gallery')),
	url(r'^projects/', include('charity_projects.urls', namespace='project')),
	url(r'^about$',  AboutView.as_view(), name='about'),
	url(r'^share$',  ShareView.as_view(), name='share'),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^$',  IndexView.as_view(), name='index'),
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
	urlpatterns += url(r'^__debug__/', include(debug_toolbar.urls)),