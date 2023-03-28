from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse("pojistenec", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ['prijmeni', 'jmeno', 'mesto']

class TypPojisteni(models.Model):

    jmeno = models.CharField('Typ pojištění', max_length=30)

    def __str__(self) -> str:
        return f'{self.jmeno}'
    
    class Meta:
        ordering = ['jmeno']

class Pojisteni(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikátní ID pojištění')
    typ_pojisteni = models.ForeignKey(TypPojisteni, on_delete=models.RESTRICT)
    pojistenec = models.ForeignKey(Pojistenec, on_delete=models.CASCADE)
    castka = models.IntegerField('Částka')
    mesicni_pojistne = models.IntegerField('Měsíční pojistné')
    platnost_od = models.DateField()
    platnost_do = models.DateField()

    predmet_pojisteni = models.CharField('Předmět pojištění', max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.typ_pojisteni.jmeno} pojištěnce {self.pojistenec.jmeno} {self.pojistenec.prijmeni}'
    
    def get_absolute_url(self):
        return reverse("pojisteni_detail", args=[self.id])

    class Meta:
        ordering = ['pojistenec__prijmeni', 'pojistenec__jmeno', 'pojistenec__mesto' ,'typ_pojisteni__jmeno']