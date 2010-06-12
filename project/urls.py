from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

groupdict = {'groupName': 'Barcamp'}

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^wiki/', include('sphene.sphwiki.urls'), groupdict), 
    url(r'^community/', include('sphene.community.urls'), groupdict),
    url(r'^$', redirect_to, {'url': '/home/'}),
    url(r'^$|^(.*)/$', 'feincms.views.applicationcontent.handler'),
)

from django.conf import settings
if getattr(settings, 'MEDIA_SERVE', False):
   urlpatterns = patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
settings.MEDIA_ROOT}),
   ) + urlpatterns

