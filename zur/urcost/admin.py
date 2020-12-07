from django.contrib import admin
from .models import PayForTag, TagToPay
from django.contrib.auth.models import Permission
from django.utils.safestring import mark_safe
from django.urls import reverse
# Register your models here.

def order_detail(obj):
    return mark_safe('<a href="{}">Podgląd</a>'.format(
        reverse('urcost:admin_order_detail', args=[obj.id])))
order_detail.short_description = 'Podgląd roliczenia'

def order_pdf(obj):
 return mark_safe('<a href="{}">PDF</a>'.format(
 reverse('urcost:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Rozliczenie PDF'



class PayForTagInline(admin.TabularInline):
    model = PayForTag
    raw_id_fields = ['tag_order']
    extra = 1

class PayForTagAdmin(admin.ModelAdmin):

    list_display = ['id', 'tag_name', 'comp_name', 'comp_local', order_detail, order_pdf]
    inlines = [PayForTagInline]



admin.site.register(TagToPay, PayForTagAdmin)
admin.site.register(PayForTag)
