# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0010_auto_20160720_0321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonialitem',
            options={'ordering': ['-order']},
        ),
        migrations.AlterField(
            model_name='testimonialitem',
            name='video',
            field=models.FileField(upload_to='testimonial_videos', blank=True),
        ),
    ]
