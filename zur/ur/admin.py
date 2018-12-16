from django.contrib import admin
from .models import Tag
from .models import Department
from .models import Priority
from .models import Work_cat
from .models import Fix_cat

# Register your models here.




admin.site.register(Department)
admin.site.register(Priority)
admin.site.register(Work_cat)
admin.site.register(Fix_cat)

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['number', 'machine', 'add_date', 'expiry_date', 'priority', 'fix_dep','manyDays']
    readonly_fields = ['manyDays']


