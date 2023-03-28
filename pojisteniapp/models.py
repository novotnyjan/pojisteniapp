from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Create your models here.

class Pojistenec(models.Model):

    jmeno = models.CharField('Jméno', max_length=30, help_text='Zadejte křestní jméno pojištěnce')
    prijmeni = models.CharField('Příjmení', max_length=30, help_text='Zadejte příjmení pojištěnce')
    email = models.EmailField(max_length=254)
    telefon = PhoneNumberField()
    ulice = models.CharField(max_length=30)
    cislo_popisne = models.IntegerField('Číslo popisné')
    mesto = models.CharField('Město', max_length=30)
    psc = models.IntegerField('PSČ', validators=[MinValueValidator(10000), MaxValueValidator(99999)])

    def __str__(self) -> str:
        return f'{self.jmeno} {self.prijmeni}'

class Pojisteni(models.Model):

    typ = models.CharField('Typ pojištění', max_length=30)

    def __str__(self) -> str:
        return f'{self.typ}'

class PojisteniInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikátní ID pojištění')
    pojisteni = models.ForeignKey(Pojisteni, on_delete=models.RESTRICT)
    pojistenec = models.ForeignKey(Pojistenec, on_delete=models.CASCADE)
    castka = models.IntegerField('Částka')
    mesicni_pojistne = models.IntegerField('Měsíční pojistné')
    platnost_od = models.DateField()
    platnost_do = models.DateField()

    predmet_pojisteni = models.CharField('Předmět pojištění', max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.pojisteni.typ} pojištěnce {self.pojistenec.jmeno} {self.pojistenec.prijmeni}'