# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonialitem',
            old_name='content',
            new_name='subtitle',
        ),
        migrations.AddField(
            model_name='testimonialitem',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
