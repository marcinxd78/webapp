from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model


# Create your models here.


class Department(models.Model):  # dodanie wydziału na zakładzie np.Magazyn
    name_dep = models.CharField(max_length=20, verbose_name='Wydział')

    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'

    def __str__(self):
        return '%s' % self.name_dep


class Priority(models.Model):  # priorytet  dodane tylk NISKI, ŚREDNI, WYSOKI
    type_prior = models.CharField(max_length=10, verbose_name='Priorytet')

    class Meta:
        verbose_name = 'Priorytet'
        verbose_name_plural = 'Priorytety'

    def __str__(self):
        return '%s' % self.type_prior


class Work_cat(models.Model):  # kategoria usterki np. niewłaściwa praca
    name_work_cat = models.CharField(max_length=30, verbose_name='Kategoria usterki')

    class Meta:
        verbose_name = 'Kategoria usterki'
        verbose_name_plural = 'Kategorie usterek'

    def __str__(self):
        return '%s' % self.name_work_cat


class Fix_cat(models.Model):  # dział odpowiedzialny za naprawe np.ELEKTRYCY
    name_fix_cat = models.CharField(max_length=20, verbose_name='Dział')

    class Meta:
        verbose_name = 'Dział'
        verbose_name_plural = 'Działy'

    def __str__(self):
        return '%s' % self.name_fix_cat


# class TagManager(models.Manager):


class Tag(models.Model):
    k = datetime.now().date()

    number = models.CharField(max_length=20, verbose_name='Numer tagu')  # numer tagu
    depart = models.ForeignKey(Department, null=True, on_delete=models.CASCADE, verbose_name='Wydział')  # wydział
    machine = models.CharField(max_length=20, verbose_name='Urządzenie')  # urządzenie
    add_date = models.DateField(verbose_name='Data dodania', default=datetime.now().date())  # data dodania
    expiry_date = models.DateField(verbose_name='Do kiedy wkonac zlecenie',
                                   default=datetime.now().date())  # data wykonania
    priority = models.ForeignKey(Priority, null=True, on_delete=models.CASCADE, verbose_name='Priorytet')  # priorytet
    explain = models.TextField(verbose_name='Opis usterki')  # opis usterki
    work_cat = models.ForeignKey(Work_cat, null=True, on_delete=models.CASCADE,
                                 verbose_name='Kategoria usterki')  # kategoria usterki
    fix_dep = models.ForeignKey(Fix_cat, null=True, on_delete=models.CASCADE,
                                verbose_name='Dział odpowiedzialny')  # kategoria działu odpowiedzialnego za usterke
    is_done = models.BooleanField(default=False, verbose_name='Czy wykonano?')  # czy naprawiono
    fix_date = models.DateField(default=datetime.now().date(), blank=True, verbose_name="Data usunięcia usterki", )

    # oblicza jaki był czas od dodania zlecenia do jego zakończenia

    def is_do_it(self):
        if self.isdone == True and self.fixdate:
            return (self.fixdate - self.add_date).days

    is_do_it.short_description = "Czas trwania zlecenia"

    # oblicza ile mamy dni na wykonanie zlecenia
    def many_days(self):
        return (self.expiry_date - self.add_date).days

    # oblicza ilść wykonanych tagów
    @classmethod
    def many_do_it(cls):
        return cls.objects.filter(is_done=True).count()

    # oblicza ilość niewykonanych tagów
    @classmethod
    def many_not_do_it(cls):
        return cls.objects.filter(is_done=False).count()

    # oblicza procent wykonanych zleceń
    @classmethod
    def percent_do_it(cls):
        count_true = cls.objects.filter(is_done=True).count()
        count_false = cls.objects.filter(is_done=False).count()
        percent_value = (count_true/(count_true + count_false))
        return format(percent_value, '.2%')

    # oblicza procent niewykonanych zleceń
    @classmethod
    def percent_not_do_it(cls):
        count_true = cls.objects.filter(is_done=True).count()
        count_false = cls.objects.filter(is_done=False).count()
        percent_value = (count_false/(count_true + count_false))
        return format(percent_value, '.2%')


    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'
        ordering = ('expiry_date',)

    def __str__(self):
        return self.number
