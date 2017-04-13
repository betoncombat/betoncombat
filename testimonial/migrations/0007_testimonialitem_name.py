# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0006_testimonialitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialitem',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]
