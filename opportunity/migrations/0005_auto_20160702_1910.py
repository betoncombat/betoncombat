# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0004_opportunityitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunityitem',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
