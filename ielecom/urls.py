from django.conf.urls import patterns, include, url
from ielecom.view import *
from maintenance.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^maintenance$', follow_d),
    url(r'^contact$', contact_tp),
    url(r'^contact_form', contact),
    url(r'^about', about),
    url(r'^download/$',download),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)