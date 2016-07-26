from __future__ import unicode_literals
from wagtail.wagtailcore.models import Page
from django.db import models
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class ArticlePage(Page):

    class HeroBlock(blocks.StructBlock):
        hero_text = blocks.RichTextBlock(blank= True,required=False)
        hero_heading = blocks.CharBlock(required=False)
        link_text = blocks.CharBlock(required=False)
        hero_image = ImageChooserBlock()
        class Meta:
            icon='image'

    class TextBlock(blocks.StructBlock):
        text = blocks.RichTextBlock(blank=True)
        class Meta:
            icon='placeholder'

    class FooterBlock(blocks.StructBlock):
        footer_text = blocks.RichTextBlock(blank= True)
        footer_image = ImageChooserBlock()
        class Meta:
            icon='placeholder'


    body = StreamField([
        ('Hero',HeroBlock()),
        ('Paragraph',TextBlock()),
        ('Footer', FooterBlock())
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
