# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 03:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('index', '0005_auto_20180504_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='image',
        ),
        migrations.AddField(
            model_name='active',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='active_image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='rsdirection',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rsdirection_image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
