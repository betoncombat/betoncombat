# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0009_testimonialvideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialvideo',
            name='inlist',
        ),
        migrations.AddField(
            model_name='testimonialitem',
            name='video',
            field=models.FileField(default='', upload_to=b'testimonial_videos'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TestimonialVideo',
        ),
    ]
