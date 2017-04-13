# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefit',
            name='subscriptonType',
            field=models.ForeignKey(default=b'', to='consulting.SubscriptionInfo'),
        ),
    ]
