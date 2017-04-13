# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0011_auto_20160608_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='show_hide_button',
            field=models.CharField(default='SHOW BUTTON', max_length=20, choices=[(b'SHOW BUTTON', b'SHOW BUTTON'), (b'HIDE BUTTON', b'HIDE BUTTON')]),
            preserve_default=False,
        ),
    ]
