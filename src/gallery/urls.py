from django.conf.urls import url
from .views import GalleryView

urlpatterns = [
    url(r'^$',  GalleryView.as_view(), name='index'),
]