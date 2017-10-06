# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-05 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0007_drivers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]