from django.db import models
from ur.models import Tag
# Create your models here.
class StatsSummary(Tag):
    class Meta:
        proxy = True
        verbose_name = 'Statystyka'
        verbose_name_plural = 'Statystyka'