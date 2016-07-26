from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import PageChooserBlock

class HomePage(Page):
    class PageBlock(blocks.StructBlock):
        heading = blocks.CharBlock(required=False)
        page_link =PageChooserBlock(required=True)
        cover = ImageChooserBlock()
        class Meta:
            icon='link'

    body = StreamField([
        ('Page',PageBlock()),
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
