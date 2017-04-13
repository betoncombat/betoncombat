# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0008_auto_20160622_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investorrelation',
            name='text',
        ),
        migrations.AddField(
            model_name='investorrelation',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
