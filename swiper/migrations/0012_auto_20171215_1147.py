# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0011_deny'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deny',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='deny',
            name='user',
        ),
        migrations.AddField(
            model_name='match',
            name='deny',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Deny',
        ),
    ]
