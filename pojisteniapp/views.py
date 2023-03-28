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
    template_name = 'pojistenec_list.html'
    paginate_by = 1