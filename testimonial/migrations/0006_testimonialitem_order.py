# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0005_remove_testimonialitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialitem',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
