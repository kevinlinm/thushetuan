# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20150416_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='game_type',
            new_name='game',
        ),
    ]
