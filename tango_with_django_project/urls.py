from django.conf.urls import patterns, include, url
from django.contrib import admin
import rango.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include(rango.urls)),
)
