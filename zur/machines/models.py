from django.db import models

# Create your models here.



class Department(models.Model):   #klasa opisująca wydział
    name_dep = models.CharField(max_length=20, verbose_name='Wydział')
    people = models.PositiveIntegerField() #ilosc osob pracujących na danym dziale
    contact = models.CharField(max_length=12, verbose_name='Numer telefonu') #telefon na wydział
    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'
    def __str__(self):
        return '%s' % self.name_dep


class PlantObjects(models.Model):
    obj_name = models.CharField(max_length=40, verbose_name='Nazwa obiektu')  # nazwa obiektu
    evidence_obj = models.CharField(max_length=40, verbose_name='Numer ewidencyjny')  # numer ewidencyjny
    obj_dep = models.ForeignKey(Department, null=True, on_delete=models.CASCADE, verbose_name='Wydział')  # wydział

    class Meta:
        verbose_name = 'Obiekt'
        verbose_name_plural = 'Obiekty'

    def __str__(self):
        return '%s' % self.obj_name


class MachineEvidence(models.Model):
    machine_symbol = models.CharField(max_length=40, verbose_name='Symbol')  # symbol urządzenia
    machine_name = models.CharField(max_length=40, verbose_name='Nazwa')  # nazwa urządzenia
    machine_depart = models.ForeignKey(Department, null=True, on_delete=models.CASCADE, verbose_name='Wydział')  # wydział na którym jest urządzenie
    serial_numb = models.CharField(max_length=30, verbose_name='Numer seryjny', null=True, blank=True)  # numer seryjny urządzenia
    evidence_numb = models.CharField(max_length=40, verbose_name='Numer ewidencyjny', null=True, blank=True)  # numer ewidencyjny
    machine_type = models.CharField(max_length=40, verbose_name='Model', null=True,blank=True)  # model urządzenia
    machine_place = models.ForeignKey(PlantObjects, null=True, on_delete=models.CASCADE, verbose_name='Lokalizacja')  # obiekt maszyny
    prod_year = models.IntegerField(verbose_name='Rok produkcji', null=True, blank=True) #rok produkcji
    usage_machine = models.BooleanField(default=True, verbose_name="W eksploatacji") #status maszyny
    machine_image = models.ImageField(upload_to='machine_img', null=True, blank=True, verbose_name='Zdjęcie')  # zdjecie
    machine_docu = models.FileField(upload_to='machine_documents', null=True, blank=True, verbose_name='Dokumentacja')  #dokumentacja

    class Meta:
        verbose_name = 'Urządzenie'
        verbose_name_plural = 'Urządzenia'

    def __str__(self):
        return '%s' % self.machine_name

