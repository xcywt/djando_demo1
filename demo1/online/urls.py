#encoding: utf-8
from django.conf.urls import url

from . import views

app_name = '[demo1]'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create/', views.create, name='create'),
	url(r'^save/', views.save, name='save'),
]
