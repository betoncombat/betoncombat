# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0008_auto_20160702_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(upload_to=b'testimonial_videos')),
                ('inlist', models.ForeignKey(to='testimonial.TestimonialItem')),
            ],
        ),
    ]
