from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pojistenec, TypPojisteni, Pojisteni

# Create your views here.

def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class PojistnecListView(generic.ListView):
    model = Pojistenec
    paginate_by = 4

class PojisteniListView(generic.ListView):
    model = Pojisteni
    paginate_by = 5

class TypPojisteniListView(generic.ListView):
    model = TypPojisteni
    paginate_by = 10
    template_name = 'pojisteniapp/typ-pojisteni_list.html'

class PojistenecDetailView(generic.DetailView):
    model = Pojistenec

class PojisteniDetailView(generic.DetailView):
    model = Pojisteni

class PojistenecCreate(CreateView):
    model = Pojistenec
    fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice', 'cislo_popisne', 'mesto', 'psc']

class PojistenecUpdate(UpdateView):
    model = Pojistenec
    fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice', 'cislo_popisne', 'mesto', 'psc']

class PojistenecDelete(DeleteView):
    model = Pojistenec
    success_url = reverse_lazy('pojistenci')

class PojisteniCreate(CreateView):
    model = Pojisteni
    fields = ['id', 'typ_pojisteni', 'pojistenec', 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']

class PojisteniUpdate(UpdateView):
    model = Pojisteni
    fields = ['id', 'typ_pojisteni', 'pojistenec', 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']

class PojisteniDelete(DeleteView):
    model = Pojisteni
    success_url = reverse_lazy('pojisteni')

class TypPojisteniCreate(CreateView):
    model = TypPojisteni
    fields = ['jmeno']
    success_url = reverse_lazy('typy-pojisteni')
    template_name = 'pojisteniapp/typ-pojisteni_form.html'

class TypPojisteniDelete(DeleteView):
    model = TypPojisteni
    success_url = reverse_lazy('typy-pojisteni')
    template_name = 'pojisteniapp/typ-pojisteni_confirm_delete.html'