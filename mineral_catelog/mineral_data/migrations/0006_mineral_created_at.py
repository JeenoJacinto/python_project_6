# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mineral_data', '0005_descriptioncount'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 17, 0, 27, 12, 686356, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
