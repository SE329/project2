# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0007_classlisting_satisfies'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlisting',
            name='coreqs',
            field=models.TextField(default='NONE'),
        ),
    ]