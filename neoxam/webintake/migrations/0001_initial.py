# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-26 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wUser',
            fields=[
                ('user_name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=15)),
                ('port_number', models.IntegerField()),
            ],
        ),
    ]