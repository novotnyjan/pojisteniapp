from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
path('o-aplikaci/', views.index, name= 'o-aplikaci'),
path('', RedirectView.as_view(url= 'o-aplikaci/')),
path('pojistenci/', views.PojistnecListView.as_view(), name= 'pojistenci'),
path('typy-pojisteni/', views.PojisteniListView.as_view(), name= 'typy-pojisteni'),
path('pojisteni_list/', views.PojisteniInstancecListView.as_view(), name= 'pojisteni_list'),
path('pojistenec/<int:pk>', views.PojistenecDetailView.as_view(), name= 'pojistenec'),
path('pojisteni_detail/<uuid:pk>', views.PojisteniInstanceDetailView.as_view(), name= 'pojisteni_detail'),
]