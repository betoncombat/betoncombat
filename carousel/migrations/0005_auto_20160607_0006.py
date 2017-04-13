# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0004_auto_20160606_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselitem',
            name='link',
        ),
        migrations.RemoveField(
            model_name='carouselitem',
            name='subtitle',
        ),
    ]
