# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-20 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0003_auto_20180820_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user_authentication.UserRole'),
        ),
    ]
