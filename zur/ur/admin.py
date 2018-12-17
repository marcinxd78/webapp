from django.contrib import admin
from .models import Tag
from .models import Department
from .models import Priority
from .models import Work_cat
from .models import Fix_cat
from django.contrib.auth.models import Permission
# Register your models here.




admin.site.register(Department)
admin.site.register(Priority)
admin.site.register(Work_cat)
admin.site.register(Fix_cat)
admin.site.register(Permission)



@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['number', 'machine', 'priority', 'add_date', 'expiry_date', 'FixDate', 'IsDone', 'fix_dep', 'manyDays', 'IsDoIt', ]
    date_hierarchy = 'expiry_date'





