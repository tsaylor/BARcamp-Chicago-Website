from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.module.blog.models import Entry
from feincms.content.richtext.models import RichTextContent
from feincms.content.image.models import ImageContent
from django.contrib.markup.templatetags.markup import textile
from django.db import models


class TextilePageContent(models.Model):
    content = models.TextField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return textile(self.content)

# feincms page stuff
Page.register_extensions('datepublisher', 'translations') # Example set of extensions

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

Page.create_content_type(TextilePageContent)




# feincms blog stuff
Entry.register_extensions('translations') # Example set of extensions

Entry.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
        ),
    })

Entry.create_content_type(RichTextContent)
Entry.create_content_type(ImageContent, POSITION_CHOICES=(
    ('block', _('block')),
    ('left', _('left')),
    ('right', _('right')),
    ))

