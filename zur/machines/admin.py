from django.contrib import admin
from .models import MachineEvidence, PlantObjects, Department
from django.contrib.auth.models import Permission


admin.site.register(PlantObjects)
admin.site.register(Department)
# Register your models here.

@admin.register(MachineEvidence)
class MachineEvidence(admin.ModelAdmin):
    list_display = ['machine_name', 'machine_depart','machine_place', ]

#admin.site.register(MachineEvidence)