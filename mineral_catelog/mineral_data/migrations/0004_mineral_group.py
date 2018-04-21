# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral_data', '0003_auto_20180322_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='group',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
    ]
