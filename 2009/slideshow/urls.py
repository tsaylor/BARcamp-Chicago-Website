from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^slides/(?P<rid>\d+)/(?P<sid>\d+)', 'slideshow.views.viewSlide'),
)