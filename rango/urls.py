from django.conf.urls import patterns, include, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^show/$', views.show, name='show'),
)
