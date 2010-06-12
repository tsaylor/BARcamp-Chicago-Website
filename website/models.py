from django.utils.translation import ugettext_lazy as _
from django.contrib.markup.templatetags.markup import textile
from django.db import models

import feincms.content.application.models as app_models
from feincms.module.page.models import Page
#from feincms.module.blog.models import Entry
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent

from sphene.sphwiki.models import WikiSnip


class TextilePageContent(models.Model):
    content = models.TextField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return textile(self.content)


class SpheneWikiPageContent(models.Model):
    snip = models.ForeignKey(WikiSnip)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        if self.snip != None:
            return """  <div class="wikicontentarea">
                            <div class="wikicontenttitle">%s</div>
                            <div class="wikicontentmain">%s</div>
                            <div class="wikicontentcontrols">
                                [ <a href="/wiki/edit/%s/" >Edit</a> ] [ <a href="/wiki/show/%s/" >Show As Wiki Page</a> ]
                            </div>
                        </div>
                    """ % (self.snip.title, self.snip.render(), self.snip.name, self.snip.name)

LINKS_CHOICES = (
    ('H', 'home'),
    ('S', 'schedule'),
    ('W', 'wiki')
    )

class SidebarLinksContent(models.Model):
    selected_button = models.CharField(max_length=1, choices=LINKS_CHOICES)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        linkHtml = lambda (initial, name) : '<div class="sidebarlink"><a href="/%s"><img src="/media/siteimages/button_%s%s.png"/></a></div>' % (
            name, name, {True: "_sel", False: ""}[initial == self.selected_button])

        return "\n".join( map( linkHtml, LINKS_CHOICES))


class Entry(models.Model):
   published_date = models.DateField()
   title = models.CharField(max_length=200)
   slug = models.SlugField()
   description = models.TextField(blank=True)

   class Meta:
       get_latest_by = 'published_date'
       ordering = ['-published_date']

   def __unicode__(self):
       return self.title

   def get_absolute_url(self):
       return "/news/%d/" % (self.id,) #('blog_entry_detail', (self.id,), {})



# feincms page stuff
Page.register_extensions('datepublisher') # Example set of extensions

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ),
    })

Page.create_content_type(RichTextContent)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('block', _('block')),
    ('left', _('left')),
    ('right', _('right')),
    ))
Page.create_content_type(app_models.ApplicationContent, APPLICATIONS=(
    ('website.entry_urls', 'News list'),
    ))

Page.create_content_type(TextilePageContent)
Page.create_content_type(SpheneWikiPageContent)
Page.create_content_type(SidebarLinksContent)


# feincms blog stuff
#Entry.register_templates({
#    'title': _('Standard template'),
#    'path': 'feincms.html',
#    'regions': (
#        ('main', _('Main content area')),
#        ),
#    })
#
#Entry.create_content_type(RichTextContent)
#Entry.create_content_type(ImageContent, POSITION_CHOICES=(
#    ('block', _('block')),
#    ('left', _('left')),
#    ('right', _('right')),
#    ))
