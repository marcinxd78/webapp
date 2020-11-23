from django.forms import ModelForm
from .models import PayForTag, TagToPay
from django import forms
from django.contrib.admin import widgets
from django.forms import inlineformset_factory

class TagToPayForm(forms.ModelForm):
    class Meta:
        model = TagToPay
        fields = ('tag_name', 'comp_name', 'comp_local', )


PayForTagFormset = inlineformset_factory(
    TagToPay, PayForTag,
    fields=('id', 'name_material', 'amount_material', 'unit', 'cost_material', ),

)