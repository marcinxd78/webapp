from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)


class MyUserManager(BaseUserManager):
    def create_user(self, email, fname, lname, position, departy, contact, brygadier, companyName,companyIn, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Użytkownik musi posiadać adres email')

        user = self.model(
            email=self.normalize_email(email),
            fname=fname,
            lname=lname,
            departy=departy,
            position=position,
            contact=contact,
            brygadier=brygadier,
            companyName=companyName,
            companyIn=companyIn,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fname, lname, position=None, departy=None, contact=None, brygadier=None, companyName=None, companyIn=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            fname=fname,
            lname=lname,
            departy=departy,
            position=position,
            contact=contact,
            brygadier=brygadier,
            companyName=companyName,
            companyIn=companyIn,
            password=password,

        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Position(models.Model):   #klasa opisująca stanowisko
    position = models.CharField(max_length=20, verbose_name='Etat')
    shift_work = models.BooleanField(default=False, verbose_name='Dostepny na zmianach') #czy dział pracuje na zmianach
    people = models.PositiveIntegerField() #ilosc osob pracujących na danym etacie
    contact = models.CharField(max_length=12, verbose_name='Numer telefonu')
    class Meta:
        verbose_name = 'Etat'
        verbose_name_plural = 'Etaty'
    def __str__(self):
        return '%s' % self.position

class Departy(models.Model):   #klasa opisująca wydział
    departy = models.CharField(max_length=20, verbose_name='Wydział')
    people = models.PositiveIntegerField() #ilosc osob pracujących na danym dziale
    contact = models.CharField(max_length=12, verbose_name='Numer telefonu') #telefon na wydział
    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'
    def __str__(self):
        return '%s' % self.departy


class MyUser(AbstractBaseUser):
    COMPANY_CHOICES = (
        ('a', 'Podwykonawca'),
        ('b', 'Własny'),
    )
    email = models.EmailField(
        verbose_name='Adres email',
        max_length=255,
        unique=True,
    )
    fname = models.CharField(max_length=50, verbose_name='Imię')
    lname = models.CharField(max_length=50, verbose_name='Nazwisko')
    position = models.ForeignKey(Position, max_length=10, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Etat') #stanowisko
    departy = models.ForeignKey(Departy, max_length=20, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Wydział') #wydział na którym pracuje
    contact = models.CharField(max_length=12, null=True, blank=True, verbose_name='Numer telefonu') #numer kontaktowy
    brygadier = models.BooleanField(default=False, null=True, blank=True, verbose_name="Brygadzista") #czy jest odpowiedzialny za dział
    companyName = models.CharField(max_length=30, null=True, blank=True, default=None, verbose_name='Nazwa firmy') #nazwa firmy
    companyIn = models.CharField(max_length=40,  null=True, blank=True, default=None, choices=COMPANY_CHOICES, verbose_name='Pracownik') #pracownik własny lub podwykonawca
    is_active = models.BooleanField(default=True, verbose_name='Aktywny?')
    is_admin = models.BooleanField(default=False, verbose_name='Administartor')
    is_staff = models.BooleanField(default=False, verbose_name='W zespole ? ')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', ]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email addres
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



    class Meta:
        verbose_name = 'Uzytkownika'
        verbose_name_plural = 'Użytkownicy'
