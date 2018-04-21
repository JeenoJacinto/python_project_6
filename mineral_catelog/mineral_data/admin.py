from django.contrib import admin

from .models import Mineral, DescriptionCount
# Register your models here.

admin.site.register(Mineral)
admin.site.register(DescriptionCount)
