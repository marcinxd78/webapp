from django.forms import ModelForm
from .models import PayForTag, TagToPay, CompanyList
from django import forms
from django.contrib.admin import widgets
from django.forms import inlineformset_factory

class TagToPayForm(forms.ModelForm):


    class Meta:
        model = TagToPay
        fields = ('tag_name', 'comp_name', )

        widgets = {
                   'tag_name': forms.Select(
                       attrs={'class': 'form-control selectpicker', 'data-live-search': 'true' , 'id': 'tag_name'}),
            'comp_name': forms.Select(
                attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'id': 'tag_name'}),
                   }

PayForTagFormset = inlineformset_factory(
    TagToPay, PayForTag,
    fields=('id', 'name_material', 'amount_material', 'unit', 'cost_material', ),
    extra=1,
)