# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20171027_1332'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='subscribe',
            new_name='subscribe_model',
        ),
    ]
