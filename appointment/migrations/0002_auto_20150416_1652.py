# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='game',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='type',
        ),
        migrations.AddField(
            model_name='ticket',
            name='game_type',
            field=models.CharField(default=b'1-2', max_length=3),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.CharField(max_length=9),
        ),
    ]
