# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_benefit_subscriptontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=300)),
                ('matter', models.TextField()),
                ('date', models.DateField()),
                ('start_time_1', models.TimeField()),
                ('start_time_2', models.TimeField()),
                ('start_time_3', models.TimeField()),
            ],
        ),
    ]
