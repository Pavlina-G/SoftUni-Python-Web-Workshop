# pets/admin.py
from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
