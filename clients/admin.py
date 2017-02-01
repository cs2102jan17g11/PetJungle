from django.contrib import admin

from models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal', 'breed')

# Register your models here.
admin.site.register(Pet, PetAdmin)
