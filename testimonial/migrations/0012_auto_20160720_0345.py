# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0011_auto_20160720_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialitem',
            name='video',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
