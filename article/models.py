from __future__ import unicode_literals
from wagtail.wagtailcore.models import Page
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import InlinePanel,FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class ArticlePage(Page):

    class HeroBlock(blocks.StructBlock):
        hero_text = blocks.RichTextBlock(blank= True,required=False)
        hero_heading = blocks.CharBlock(required=False)
        link_text = blocks.CharBlock(required=False)
        link_location = blocks.CharBlock(required=False)
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

    class ImageSliderBlock(blocks.StructBlock):
         slide = blocks.StructBlock([
             ('Image',ImageChooserBlock()),
             ('Caption',  blocks.RichTextBlock(blank=True)),
         ])
         class Meta:
             icon='image'

    body = StreamField([
        ('Hero',HeroBlock()),
        ('Paragraph',TextBlock()),
        ('Footer', FooterBlock()),
        ('Carousel', blocks.ListBlock(ImageSliderBlock()))
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
