from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import ideas.views as views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home),
    url(r'^idea/(?P<idea_id>\d+)/(?P<slug>.*)/$', views.idea),
    # url(r'^ideas/', include('ideas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
