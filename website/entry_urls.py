from django.conf.urls.defaults import *
from feincms.module.blog.models import Entry

entry_dict = {'queryset': Entry.objects.all()}

urlpatterns = patterns('',
   url(r'^$',
       'feincms.views.generic.list_detail.object_list',
       dict(entry_dict, **{'template_name': 'news/entry_list.html'}),
       name='blog_entry_list'),
   url(r'^news/(?P<object_id>\d+)/$',
       'feincms.views.generic.list_detail.object_detail',
       dict(entry_dict, **{'template_name': 'news/entry_detail.html'}),
       name='blog_entry_detail'),
)

