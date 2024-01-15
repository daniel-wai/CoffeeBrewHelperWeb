from django.contrib import admin
from .models import Step, BrewStep, Recipe, BrewMethod
from adminsortable2.admin import SortableAdminMixin

class StepAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('step_id','__str__','recipe','description')

admin.site.register(Step, StepAdmin)

class BrewStepAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__str__','change_in_water', 'change_in_time')

admin.site.register(BrewStep, BrewStepAdmin)

class RecipeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('recipe_id','name','description')

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(BrewMethod)


