# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([('Hero', wagtail.wagtailcore.blocks.StructBlock([(b'hero_text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'hero_image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('Paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True))])), ('Footer', wagtail.wagtailcore.blocks.StructBlock([(b'footer_text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'footer_image', wagtail.wagtailimages.blocks.ImageChooserBlock())]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]