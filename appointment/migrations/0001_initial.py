# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=8)),
                ('number', models.SmallIntegerField(default=6)),
                ('game', models.SmallIntegerField(default=1)),
                ('type', models.SmallIntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thu_id', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=11)),
                ('ticket', models.ForeignKey(to='appointment.Ticket')),
            ],
        ),
    ]
