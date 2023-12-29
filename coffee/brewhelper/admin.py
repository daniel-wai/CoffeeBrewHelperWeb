from django.contrib import admin
from .models import BrewStep, Recipe
from adminsortable2.admin import SortableAdminMixin

class BrewStepAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('step_id','__str__','recipeID','description', 'change_in_water', 'change_in_time')

admin.site.register(BrewStep, BrewStepAdmin)

class RecipeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('recipe_id','name','description')

admin.site.register(Recipe, RecipeAdmin)
