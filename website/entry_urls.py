from django.conf.urls.defaults import *
from feincms.module.blog.models import Entry

entry_dict = {'queryset': Entry.objects.all()}

urlpatterns = patterns('',
   url(r'^$',
       'feincms.views.generic.list_detail.object_list',
       entry_dict,
       name='entry_list'),
   url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[^/]+)/',
       'feincms.views.generic.date_based.object_detail',
       dict(entry_dict, **{'date_field': 'published_date', 'month_format': '%m', 'slug_field': 'slug'}),
       name='entry_detail'),
)

