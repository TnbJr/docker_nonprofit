from django.conf.urls import url
from .views import CharityProjectIndexView, CharityProjectDetailView

urlpatterns = [
	url(r'^$',  CharityProjectIndexView.as_view(), name='index'),
	url(r'^(?P<slug>[\w-]+)$',  CharityProjectDetailView.as_view(), name='detail'),
]