# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0002_auto_20160613_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonialitem',
            old_name='subtitle',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='testimonialitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='testimonialitem',
            name='title',
        ),
    ]
