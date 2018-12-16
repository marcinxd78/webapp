from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.



class Department(models.Model):  #dodanie wydziału na zakładzie np.Magazyn
    name_dep = models.CharField(max_length=20, verbose_name='Wydział')

    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'

    def __str__(self):
        return '%s' % self.name_dep



class Priority(models.Model):   #priorytet  dodane tylk NISKI, ŚREDNI, WYSOKI
    type_prior = models.CharField(max_length=10, verbose_name='Priorytet')

    class Meta:
        verbose_name = 'Priorytet'
        verbose_name_plural = 'Priorytety'

    def __str__(self):
        return '%s' % self.type_prior


class Work_cat(models.Model):  #kategoria usterki np. niewłaściwa praca
    name_work_cat = models.CharField(max_length=30, verbose_name='Kategoria usterki')

    class Meta:
        verbose_name = 'Kategoria usterki'
        verbose_name_plural = 'Kategorie usterek'

    def __str__(self):
        return '%s' % self.name_work_cat


class Fix_cat(models.Model):   #dział odpowiedzialny za naprawe np.ELEKTRYCY
    name_fix_cat = models.CharField(max_length=20, verbose_name='Dział')

    class Meta:
        verbose_name = 'Dział'
        verbose_name_plural = 'Działy'

    def __str__(self):
        return '%s' % self.name_fix_cat


class Tag(models.Model):


    number = models.CharField(max_length=20, verbose_name='Numer tagu')  #numer tagu
    depart = models.ForeignKey(Department, null=True,  on_delete=models.CASCADE, verbose_name='Wydział') #wydział
    machine = models.CharField(max_length=20, verbose_name='Urządzenie') #urządzenie
    add_date = models.DateField(verbose_name='Data dodania') #data dodania
    expiry_date = models.DateField(verbose_name='Data wykonania') #data wykonania
    priority = models.ForeignKey(Priority, null=True, on_delete=models.CASCADE, verbose_name='Priorytet') #priorytet
    explain = models.TextField(verbose_name='Opis usterki') #opis usterki
    work_cat = models.ForeignKey(Work_cat, null=True, on_delete=models.CASCADE, verbose_name='Kategoria usterki') #kategoria usterki
    fix_dep = models.ForeignKey(Fix_cat, null=True, on_delete=models.CASCADE, verbose_name='Dział odpowiedzialny') #kategoria działu odpowiedzialnego za usterke

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'
        ordering = ('expiry_date',)

    def __str__(self):
     return self.number



