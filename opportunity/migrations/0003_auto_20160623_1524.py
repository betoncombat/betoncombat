# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0002_opportunityitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunityitem',
            name='image',
            field=models.ImageField(upload_to=b'media/opportunity/', blank=True),
        ),
    ]
