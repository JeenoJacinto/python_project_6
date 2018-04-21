import json, os, random

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.db import transaction

from .models import Mineral, DescriptionCount

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    pk_list = []
    for model in minerals:
        pk_list.append(model.pk)
    random_pk = random.randint(min(pk_list), max(pk_list))
    return render(
        request,
        'mineral_data/mineral_list.html',
        {'minerals': minerals, 'random_pk': random_pk},
    )


def mineral_detail(request, pk):
    minerals = Mineral.objects.all()
    pk_list = []
    for model in minerals:
        pk_list.append(model.pk)
    random_pk = random.randint(min(pk_list), max(pk_list))
    mineral = get_object_or_404(Mineral, pk=pk)
    ordering_list = []
    attribute_count = DescriptionCount.objects.get().__dict__
    for attr, value in attribute_count.items():
        # parsing values based on relevance of data
        if attr == '_state':
            continue
        elif attr == 'name':
            continue
        elif attr == 'image_caption':
            continue
        elif attr == 'image_filename':
            continue
        elif attr == 'id':
            continue
        else:
            ordering_list.append(value)
    sorted_list = sorted(ordering_list, reverse=True)
    # sorted list will store the selected mineral's data in order of
    # the most common attribute to the least excluding a few
    used_attr_list = [] # eliminates matching complications
    for idx, data in enumerate(sorted_list):
        # numerically sorted list now ranking attributes
        for attr, value in attribute_count.items():
            if not attr in used_attr_list:
                if data == value:
                    if attr == '_state':
                        continue
                    elif attr == 'name':
                        continue
                    elif attr == 'image_caption':
                        continue
                    elif attr == 'image_filename':
                        continue
                    elif attr == 'id':
                        continue
                    else:
                        sorted_list[idx] = {idx:attr}
                        used_attr_list.append(attr)
    sorted_list = []
    for key, value in enumerate(used_attr_list):
        sorted_list.append({key:value})

    relevance_list = [] # keeps track of description name
    for item in sorted_list:
        relevance_list.append(item)
    for item in sorted_list:
        for key, value in item.items():
        # storing specific model data in order based on data relevance
        # stored in sorted_list
            if value == 'category':
                sorted_list[key] = mineral.category
            elif value == 'formula':
                sorted_list[key] = mineral.formula
            elif value == 'strunz_classification':
                sorted_list[key] = mineral.strunz_classification
            elif value == 'color':
                sorted_list[key] = mineral.color
            elif value == 'crystal_system':
                sorted_list[key] = mineral.crystal_system
            elif value == 'unit_cell':
                sorted_list[key] = mineral.unit_cell
            elif value == 'crystal_symmetry':
                sorted_list[key] = mineral.crystal_symmetry
            elif value == 'cleavage':
                sorted_list[key] = mineral.cleavage
            elif value == 'mohs_scale_hardness':
                sorted_list[key] = mineral.mohs_scale_hardness
            elif value == 'luster':
                sorted_list[key] = mineral.luster
            elif value == 'streak':
                sorted_list[key] = mineral.streak
            elif value == 'diaphaneity':
                sorted_list[key] = mineral.diaphaneity
            elif value == 'optical_properties':
                sorted_list[key] = mineral.optical_properties
            elif value == 'refractive_index':
                sorted_list[key] = mineral.refractive_index
            elif value == 'crystal_habit':
                sorted_list[key] = mineral.crystal_habit
            elif value == 'specific_gravity':
                sorted_list[key] = mineral.specific_gravity
            elif value == 'group':
                sorted_list[key] = mineral.group
    fmt_relevance_list = []
    for item in relevance_list:
        for key, value in item.items():
            fmt_relevance_list.append({key:value.replace('_', ' ')})
    return render(
        request,
        'mineral_data/mineral_detail.html',
        {
            'mineral': mineral,
            'sorted_details': sorted_list,
            'relevance_details': fmt_relevance_list,
            'random_pk': random_pk
        }
    )
