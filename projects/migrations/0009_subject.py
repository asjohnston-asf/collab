# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160503_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('dewey_class_code', models.CharField(max_length=3)),
                ('color_code', models.CharField(max_length=7)),
            ],
        ),
    ]
