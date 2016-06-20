# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CellDoor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('door_number', models.IntegerField()),
                ('unlocked', models.BooleanField()),
                ('secured', models.BooleanField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
    ]
