# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0003_auto_20160623_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunityitem',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
