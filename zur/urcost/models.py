from django.db import models
from ur.models import Tag

# Create your models here.

app_name = 'urcost'


class CompanyList(models.Model):
    cmp_name = models.CharField(max_length=50, verbose_name='Nazwa firmy')
    cmp_address = models.CharField(max_length=50, verbose_name='Adres')
    cmp_address2 = models.CharField(max_length=50, verbose_name='Adres cd.')
    cmp_tel = models.CharField(max_length=50, verbose_name='Numer telefonu')

    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firmy'

    def __str__(self):
        return '%s' % self.cmp_name


class TagToPay(models.Model):
    tag_name = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE, verbose_name='Nazwa zlecenia')  # wydział
    comp_name = models.ForeignKey(CompanyList, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rozliczenie'
        verbose_name_plural = 'Rozliczenia'

    def __str__(self):
        return '%s' % self.id

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class PayForTag(models.Model):
    UNIT_CHOICES = (
        ('a', 'godzina'),
        ('b', 'metr'),
        ('c', 'sztuk'),
        ('d', 'kilogram')
    )
    tag_order = models.ForeignKey(TagToPay, null=True, on_delete=models.CASCADE)  # wydział
    name_material = models.CharField(max_length=20, verbose_name='Materiał')
    amount_material = models.PositiveIntegerField(default=1, verbose_name='Ilość')
    unit = models.CharField(max_length=40, null=True, blank=True, default=None, choices=UNIT_CHOICES,
                            verbose_name='Jednostka')
    cost_material = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')

    class Meta:
        verbose_name = 'Materiał'
        verbose_name_plural = 'Materiały'

    def __str__(self):
        return '%s' % self.id

    def get_cost(self):
        return self.amount_material * self.cost_material
