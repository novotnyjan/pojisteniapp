from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pojistenec, TypPojisteni, Pojisteni

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

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
    fields = ['typ_pojisteni', 'pojistenec', 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']

class PojisteniUpdate(UpdateView):
    model = Pojisteni
    fields = ['typ_pojisteni', 'pojistenec', 'castka', 'mesicni_pojistne', 'platnost_od', 'platnost_do', 'predmet_pojisteni']

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


from .forms import PojistitPojistenceForm, VytvoritPojisteniForm

def pojistit_pojistence(request, pk):
    pojistenec = get_object_or_404(Pojistenec, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = PojistitPojistenceForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():


            pojisteni = Pojisteni(typ_pojisteni= form.cleaned_data['typ_pojisteni'],
                                  pojistenec = pojistenec,
                                  castka = form.cleaned_data['castka'],
                                  mesicni_pojistne = form.cleaned_data['mesicni_pojistne'],
                                  platnost_od = form.cleaned_data['platnost_od'],
                                  platnost_do = form.cleaned_data['platnost_do'],
                                  predmet_pojisteni = form.cleaned_data['predmet_pojisteni'],
                                  )
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            pojisteni.save()

            # redirect to a new URL:
            return HttpResponseRedirect(pojistenec.get_absolute_url())

    # If this is a GET (or any other method) create the default form.
    else:
        form = PojistitPojistenceForm(initial={'pojistenec': pojistenec.pk})

    context = {
        'form': form,
        'pojistenec': pojistenec
    }

    return render(request, 'pojisteniapp/pojisteni-pojistence_form.html', context)


from django.urls import reverse

def vytvorit_pojisteni(request):
    import uuid
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = VytvoritPojisteniForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            form.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('pojisteni_list'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = VytvoritPojisteniForm()

    context = {
        'form': form,
    }

    return render(request, 'pojisteniapp/pojisteni_form.html', context)

def upravit_pojisteni(request, pk):
    pojisteni = get_object_or_404(Pojisteni, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = VytvoritPojisteniForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            pojisteni.typ_pojisteni= form.cleaned_data['typ_pojisteni']
            pojisteni.pojistenec = form.cleaned_data['pojistenec']
            pojisteni.castka = form.cleaned_data['castka']
            pojisteni.mesicni_pojistne = form.cleaned_data['mesicni_pojistne']
            pojisteni.platnost_od = form.cleaned_data['platnost_od']
            pojisteni.platnost_do = form.cleaned_data['platnost_do']
            pojisteni.predmet_pojisteni = form.cleaned_data['predmet_pojisteni']
            pojisteni.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('pojisteni_list'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = VytvoritPojisteniForm(initial={
            'typ_pojisteni':pojisteni.typ_pojisteni,
            'pojistenec':pojisteni.pojistenec,
            'castka':pojisteni.castka,
            'mesicni_pojistne':pojisteni.mesicni_pojistne,
            'platnost_od': pojisteni.platnost_od,
            'platnost_do': pojisteni.platnost_do,
            'predmet_pojisteni': pojisteni.predmet_pojisteni,
        })

    context = {
        'form': form,
    }

    return render(request, 'pojisteniapp/pojisteni_form.html', context)