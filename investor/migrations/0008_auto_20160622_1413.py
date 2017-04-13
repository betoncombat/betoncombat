# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0007_auto_20160622_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorrelation',
            name='text',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
