from django.urls import re_path

from . import views

urlpatterns = [
	re_path(r'^(.+)\.(nt|ttl|rdf|json)$', views.dumpdata, name='dump'),
]
