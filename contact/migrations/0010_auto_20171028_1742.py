# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20171028_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe_model',
            name='post',
        ),
        migrations.AddField(
            model_name='subscribe_model',
            name='Email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
