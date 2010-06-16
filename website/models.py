from django.utils.translation import ugettext_lazy as _
from django.contrib.markup.templatetags.markup import textile
from django.db import models

import feincms.content.application.models as app_models
from feincms.module.page.models import Page
#from feincms.module.blog.models import Entry
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent

from sphene.sphwiki.models import WikiSnip

import re

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
    ('W', 'wiki'),
    ('T', 'what'),
    ('O', 'who'),
    ('E', 'where'),
    ('A', 'agenda'),
    ('P', 'helpout'),
    ('C', 'community'),
    )

def rendersidebar(page):
    linkHtml = lambda (initial, name) : '<div class="sidebarlink"><a href="/%s"><img src="/media/siteimages/button_%s%s.png"/></a></div>' % (
        name, name, {True: "_sel", False: ""}[initial == page])

    return "\n".join( map( linkHtml, LINKS_CHOICES))
   

class SidebarLinksContent(models.Model):
    selected_button = models.CharField(max_length=1, choices=LINKS_CHOICES)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return rendersidebar(self.selected_button)

class YoutubeContent(models.Model):
    youtube_id = models.CharField(max_length=40, default="")

    class Meta:
        abstract = True

    def render(self, **kwargs):
        if self.youtube_id != "": 
            return """
                <object style="display:inline;" width="425" height="344">
                    <param name="movie" value="http://youtube.com/v/%s&amp;hl=en&amp;fs=1">
                    </param>
                    <param name="allowFullScreen" value="true">
                    </param>
                    <embed style="display:inline;" src="http://youtube.com/v/%s&amp;hl=en&amp;fs=1" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344">
                    </embed>
                </object>
                """ % (self.youtube_id, self.youtube_id)
        else:
            return ""

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
Page.create_content_type(YoutubeContent)


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
