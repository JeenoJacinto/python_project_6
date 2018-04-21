# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=1000, default='')),
                ('image_filename', models.CharField(max_length=1000, default='')),
                ('image_caption', models.CharField(max_length=1000, default='')),
                ('category', models.CharField(max_length=1000, default='')),
                ('formula', models.CharField(max_length=1000, default='')),
                ('strunz_classification', models.CharField(max_length=1000, default='')),
                ('color', models.CharField(max_length=1000, default='')),
                ('crystal_system', models.CharField(max_length=1000, default='')),
                ('unit_cell', models.CharField(max_length=1000, default='')),
                ('crystal_symmetry', models.CharField(max_length=1000, default='')),
                ('cleavage', models.CharField(max_length=1000, default='')),
                ('mohs_scale_hardness', models.CharField(max_length=1000, default='')),
                ('luster', models.CharField(max_length=1000, default='')),
                ('streak', models.CharField(max_length=1000, default='')),
                ('optical_properties', models.CharField(max_length=1000, default='')),
                ('refractive_index', models.CharField(max_length=1000, default='')),
                ('crystal_habit', models.CharField(max_length=1000, default='')),
                ('specific_gravity', models.CharField(max_length=1000, default='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
