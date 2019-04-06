from django.conf.urls import url
from django.urls import path

from .views import list_blogs

urlpatterns = [
    url('^$', list_blogs, name='list_blogs'),
    path('archive/<int:year>/', list_blogs, name='list_archived_blogs')
]