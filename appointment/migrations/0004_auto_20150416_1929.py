# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20150416_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='game_type',
            field=models.IntegerField(default=1),
        ),
    ]
