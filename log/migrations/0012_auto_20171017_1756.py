# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_sensordata_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanvalidationdata',
            name='fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='humanvalidationdata',
            name='passengers',
            field=models.IntegerField(null=True),
        ),
    ]
