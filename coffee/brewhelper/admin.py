from django.contrib import admin
from .models import brewstep
from adminsortable2.admin import SortableAdminMixin

class BrewStepAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('step_id','__str__', 'change_in_water', 'change_in_time')

admin.site.register(brewstep, BrewStepAdmin)
