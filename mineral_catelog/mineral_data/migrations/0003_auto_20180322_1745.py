# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral_data', '0002_mineral_diaphaneity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='category',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='color',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_habit',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_symmetry',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='formula',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_caption',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image_filename',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='mohs_scale_hardness',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='name',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_classification',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='unit_cell',
            field=models.CharField(max_length=1000, blank=True, default=''),
        ),
    ]
