import json, os, random

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.db import transaction

from mineral_data.models import Mineral, DescriptionCount

def home(request):
    minerals = Mineral.objects.all()
    description_count = DescriptionCount.objects.all()
    if not minerals:
        # if there is no data then data will be upload from json file
        with open(
            os.path.join(
                settings.BASE_DIR, r'mineral_data\data\minerals.json'
            ),
            encoding="utf8"
        ) as json_file:
            data = json.load(json_file)
            with transaction.atomic():
                for item in data:
                    # replace key spaces with underscores for this to work
                    formatted_kwargs = {}
                    for field in item:
                        formatted_kwargs[field.replace(' ', '_')] = item[field]
                        # replaces spaces with underscore to fit model fields
                    obj = Mineral(**formatted_kwargs)
                    obj.save()
        minerals = Mineral.objects.all()
        # minerals variable updated with all the new models
    if not description_count:
        detail_count_kwargs = {
            'name': 0,
            'image_filename': 0,
            'image_caption': 0,
            'category': 0,
            'formula': 0,
            'strunz_classification': 0,
            'color': 0,
            'crystal_system': 0,
            'unit_cell': 0,
            'crystal_symmetry': 0,
            'cleavage': 0,
            'mohs_scale_hardness': 0,
            'luster': 0,
            'streak': 0,
            'diaphaneity': 0,
            'optical_properties': 0,
            'refractive_index': 0,
            'crystal_habit': 0,
            'specific_gravity': 0,
            'group': 0
        }
        for mineral in minerals:
            if mineral.name:
                detail_count_kwargs['name'] = detail_count_kwargs['name'] + 1
            if mineral.image_filename:
                detail_count_kwargs['image_filename'] = detail_count_kwargs[
                    'image_filename'
                ] + 1
            if mineral.image_caption:
                detail_count_kwargs['image_caption'] = detail_count_kwargs[
                    'image_caption'
                ] + 1
            if mineral.category:
                detail_count_kwargs['category'] = detail_count_kwargs[
                    'category'
                ] + 1
            if mineral.formula:
                detail_count_kwargs['formula'] = detail_count_kwargs[
                    'formula'
                ] + 1
            if mineral.strunz_classification:
                detail_count_kwargs[
                    'strunz_classification'
                ] = detail_count_kwargs['strunz_classification'] + 1
            if mineral.color:
                detail_count_kwargs['color'] = detail_count_kwargs['color'] + 1
            if mineral.crystal_system:
                detail_count_kwargs['crystal_system'] = detail_count_kwargs[
                    'crystal_system'
                ] + 1
            if mineral.unit_cell:
                detail_count_kwargs['unit_cell'] = detail_count_kwargs[
                    'unit_cell'
                ] + 1
            if mineral.crystal_symmetry:
                detail_count_kwargs['crystal_symmetry'] = detail_count_kwargs[
                    'crystal_symmetry'
                ] + 1
            if mineral.cleavage:
                detail_count_kwargs['cleavage'] = detail_count_kwargs[
                    'cleavage'
                ] + 1
            if mineral.mohs_scale_hardness:
                detail_count_kwargs[
                    'mohs_scale_hardness'
                ] = detail_count_kwargs['mohs_scale_hardness'] + 1
            if mineral.luster:
                detail_count_kwargs['luster'] = detail_count_kwargs[
                    'luster'
                ] + 1
            if mineral.streak:
                detail_count_kwargs['streak'] = detail_count_kwargs[
                    'streak'
                ] + 1
            if mineral.diaphaneity:
                detail_count_kwargs['diaphaneity'] = detail_count_kwargs[
                    'diaphaneity'
                ] + 1
            if mineral.optical_properties:
                detail_count_kwargs[
                    'optical_properties'
                ] = detail_count_kwargs['optical_properties'] + 1
            if mineral.refractive_index:
                detail_count_kwargs[
                    'refractive_index'
                ] = detail_count_kwargs['refractive_index'] + 1
            if mineral.crystal_habit:
                detail_count_kwargs[
                    'crystal_habit'
                ] = detail_count_kwargs['crystal_habit'] + 1
            if mineral.specific_gravity:
                detail_count_kwargs[
                    'specific_gravity'
                ] = detail_count_kwargs['specific_gravity'] + 1
        obj = DescriptionCount(**detail_count_kwargs)
        obj.save()
    all_minerals = Mineral.objects.all()
    description_count = DescriptionCount.objects.get()
    attribute_count = DescriptionCount.objects.get().__dict__
    attribute_count.pop('_state', None)
    attribute_count.pop('id', None)
    num_of_minerals = len(all_minerals)
    fmt_attribute_count = {} # replaces underscores with spaces
    for key, value in attribute_count.items():
        fmt_attribute_count[key.replace("_", " ")] = value
    return render(
        request,
        'home.html',
        {
            'num_of_minerals': num_of_minerals,
            'attribute_count': fmt_attribute_count
        }
    )
