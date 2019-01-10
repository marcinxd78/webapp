from django.forms import ModelForm
from .models import Tag


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['number', 'depart', 'machine', 'add_date',
                  'expiry_date', 'priority', 'explain', 'work_cat', 'fix_dep',
                  'is_done', 'fix_date', ]
