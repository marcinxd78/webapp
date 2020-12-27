from django.forms import ModelForm
from .models import Tag
from django import forms
from django.contrib.admin import widgets
class DateInput(forms.DateInput):
    input_type = 'date'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['number', 'depart', 'machine', 'add_date',
                  'expiry_date', 'priority', 'explain', 'work_cat', 'fix_dep',
                  'is_done','image', 'fix_date', ]
       #format- formatowanie daty i godziny aby mozna było ja pobrac z bazy danych
        widgets = {'add_date': DateInput(format = '%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}), 'expiry_date': DateInput(format = '%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}),
                   'fix_date': DateInput(format ='%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}),
                   'machine': forms.Select(
                       attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
                   }



