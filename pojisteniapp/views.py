from django.shortcuts import render
from django.views import generic
from .models import Pojistenec, Pojisteni, PojisteniInstance

# Create your views here.

def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class PojistnecListView(generic.ListView):
    model = Pojistenec
    paginate_by = 5

class PojisteniInstancecListView(generic.ListView):
    model = PojisteniInstance
    paginate_by = 5
    template_name = 'pojisteniapp/pojisteni-instance_list.html'

class PojisteniListView(generic.ListView):
    model = Pojisteni
    paginate_by = 10

class PojistenecDetailView(generic.DetailView):
    model = Pojistenec

class PojisteniInstanceDetailView(generic.DetailView):
    model = PojisteniInstance
    template_name = 'pojisteniapp/pojisteni-instance_detail.html'