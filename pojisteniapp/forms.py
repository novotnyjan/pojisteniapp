from django.forms import ModelForm
from django import forms
from .models import Pojisteni

class PojistitPojistenceForm(ModelForm):
    class Meta:
        model = Pojisteni
        fields = ['typ_pojisteni', 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']
        widgets = {
            'platnost_od' : forms.SelectDateWidget,
            'platnost_do' : forms.SelectDateWidget,
        }

class VytvoritPojisteniForm(ModelForm):
    class Meta:
        model = Pojisteni
        fields = ['typ_pojisteni', 'pojistenec' , 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']
        widgets = {
            'platnost_od' : forms.SelectDateWidget,
            'platnost_do' : forms.SelectDateWidget,
        }