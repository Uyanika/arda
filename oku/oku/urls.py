from django.conf.urls import patterns, include, url
import views, views_2
 # -*- coding: UTF-8 -*-

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^Dest', views.Dest),
    #url(r'^search_form/$', views.search_form),
    url(r'^search', views.search),
    #url(r'^geometry', views.geometry),
    # url(r'^oku/', include('oku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
