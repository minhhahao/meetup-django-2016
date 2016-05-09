# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('tile', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
