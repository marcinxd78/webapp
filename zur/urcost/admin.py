from django.contrib import admin
from .models import PayForTag, TagToPay
from django.contrib.auth.models import Permission
# Register your models here.


class PayForTagInline(admin.TabularInline):
    model = PayForTag


class PayForTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag_name', 'comp_name', 'comp_local']
    inlines = [PayForTagInline]


admin.site.register(TagToPay, PayForTagAdmin)