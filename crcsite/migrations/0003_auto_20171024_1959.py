# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcsite', '0002_answer_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='Value',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]
