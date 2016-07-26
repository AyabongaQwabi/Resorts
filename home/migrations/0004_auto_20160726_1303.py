# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 13:03
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160726_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='page_link',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('Page', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), (b'cover', wagtail.wagtailimages.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
    ]