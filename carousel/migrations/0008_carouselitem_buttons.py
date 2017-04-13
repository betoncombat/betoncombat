# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0007_auto_20160607_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='buttons',
            field=models.CharField(default='AN', max_length=2, choices=[(b'RM', b'READ MORE'), (b'LM', b'LEARN MORE'), (b'AN', b'APPLY NOW')]),
            preserve_default=False,
        ),
    ]
