# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0012_carouselitem_show_hide_button'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carouselitem',
            old_name='show_hide_button',
            new_name='show_or_hide_button',
        ),
    ]
