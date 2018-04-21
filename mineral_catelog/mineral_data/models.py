from django.db import models


class Mineral(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1000, default='', blank=True)
    image_filename = models.CharField(max_length=1000, default='', blank=True)
    image_caption = models.CharField(max_length=1000, default='', blank=True)
    category = models.CharField(max_length=1000, default='', blank=True)
    formula = models.CharField(max_length=1000, default='', blank=True)
    strunz_classification = models.CharField(
        max_length=1000, default='', blank=True
    )
    color = models.CharField(max_length=1000, default='', blank=True)
    crystal_system = models.CharField(max_length=1000, default='', blank=True)
    unit_cell = models.CharField(max_length=1000, default='', blank=True)
    crystal_symmetry = models.CharField(
        max_length=1000, default='', blank=True
    )
    cleavage = models.CharField(max_length=1000, default='', blank=True)
    mohs_scale_hardness = models.CharField(
        max_length=1000, default='', blank=True
    )
    luster = models.CharField(max_length=1000, default='', blank=True)
    streak = models.CharField(max_length=1000, default='', blank=True)
    diaphaneity = models.CharField(max_length=1000, default='', blank=True)
    optical_properties = models.CharField(
        max_length=1000, default='', blank=True
    )
    refractive_index = models.CharField(
        max_length=1000, default='', blank=True
    )
    crystal_habit = models.CharField(max_length=1000, default='', blank=True)
    specific_gravity = models.CharField(
        max_length=1000, default='', blank=True
    )
    group = models.CharField(max_length=1000, default='', blank=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name


class DescriptionCount(models.Model):
    """Stores the count for attribute relevance"""
    name = models.IntegerField(default=0)
    image_filename = models.IntegerField(default=0)
    image_caption = models.IntegerField(default=0)
    category = models.IntegerField(default=0)
    formula = models.IntegerField(default=0)
    strunz_classification = models.IntegerField(default=0)
    color = models.IntegerField(default=0)
    crystal_system = models.IntegerField(default=0)
    unit_cell = models.IntegerField(default=0)
    crystal_symmetry = models.IntegerField(default=0)
    cleavage = models.IntegerField(default=0)
    mohs_scale_hardness = models.IntegerField(default=0)
    luster = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    diaphaneity = models.IntegerField(default=0)
    optical_properties = models.IntegerField(default=0)
    refractive_index = models.IntegerField(default=0)
    crystal_habit = models.IntegerField(default=0)
    specific_gravity = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
