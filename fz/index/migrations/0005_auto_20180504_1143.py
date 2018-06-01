# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 03:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('index', '0004_auto_20180504_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paperimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='paperimage',
            name='title',
        ),
        migrations.AddField(
            model_name='paper',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.DeleteModel(
            name='PaperImage',
        ),
    ]