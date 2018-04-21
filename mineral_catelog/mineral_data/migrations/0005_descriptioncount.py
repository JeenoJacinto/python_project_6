# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral_data', '0004_mineral_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.IntegerField(default=0)),
                ('image_filename', models.IntegerField(default=0)),
                ('image_caption', models.IntegerField(default=0)),
                ('category', models.IntegerField(default=0)),
                ('formula', models.IntegerField(default=0)),
                ('strunz_classification', models.IntegerField(default=0)),
                ('color', models.IntegerField(default=0)),
                ('crystal_system', models.IntegerField(default=0)),
                ('unit_cell', models.IntegerField(default=0)),
                ('crystal_symmetry', models.IntegerField(default=0)),
                ('cleavage', models.IntegerField(default=0)),
                ('mohs_scale_hardness', models.IntegerField(default=0)),
                ('luster', models.IntegerField(default=0)),
                ('streak', models.IntegerField(default=0)),
                ('diaphaneity', models.IntegerField(default=0)),
                ('optical_properties', models.IntegerField(default=0)),
                ('refractive_index', models.IntegerField(default=0)),
                ('crystal_habit', models.IntegerField(default=0)),
                ('specific_gravity', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=0)),
            ],
        ),
    ]
