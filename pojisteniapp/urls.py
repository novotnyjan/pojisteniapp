from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
path('o-aplikaci/', views.index, name= 'o-aplikaci'),
path('', RedirectView.as_view(url= 'o-aplikaci/')),
path('pojistenci', views.PojistnecListView.as_view(), name= 'pojistenci')
]