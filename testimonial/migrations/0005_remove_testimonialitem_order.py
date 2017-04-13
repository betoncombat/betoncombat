# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0004_testimonialitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialitem',
            name='order',
        ),
    ]
