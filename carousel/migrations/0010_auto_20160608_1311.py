# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0009_auto_20160608_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='buttons',
            field=models.CharField(blank=True, max_length=20, choices=[(b'READ MORE', b'READ MORE'), (b'LEARN MORE', b'LEARN MORE'), (b'APPLY NOW', b'APPLY NOW')]),
        ),
    ]
