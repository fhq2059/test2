# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-31 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20180502_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': '人员', 'verbose_name_plural': '人员'},
        ),
    ]