# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0007_testimonialitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialitem',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
