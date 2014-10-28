from django.conf.urls import patterns, url
from app1 import views


urlpatterns = patterns('',
						url(r'^registration$', views.registration, name='registration'),
						url(r'^login$', views.login, name='login'),


)
