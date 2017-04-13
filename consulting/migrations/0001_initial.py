# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionInfo',
            fields=[
                ('duration', models.CharField(max_length=1, unique=True, serialize=False, primary_key=True, choices=[(b'W', b'weekly'), (b'M', b'monthly'), (b'Y', b'annually')])),
                ('price', models.DecimalField(max_digits=25, decimal_places=2)),
            ],
        ),
    ]
