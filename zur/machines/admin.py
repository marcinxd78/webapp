from django.contrib import admin
from .models import MachineEvidence, PlantObjects, Department
from django.contrib.auth.models import Permission

admin.site.register(MachineEvidence)
admin.site.register(PlantObjects)
admin.site.register(Department)
# Register your models here.
