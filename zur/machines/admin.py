from django.contrib import admin
from .models import MachineEvidence, PlantObjects
from django.contrib.auth.models import Permission

admin.site.register(MachineEvidence)
admin.site.register(PlantObjects)
# Register your models here.
