# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-02 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20171002_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
