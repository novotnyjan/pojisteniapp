from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
path('o-aplikaci/', views.index, name= 'o-aplikaci'),
path('', RedirectView.as_view(url= 'o-aplikaci/')),
path('pojistenci/', views.PojistnecListView.as_view(), name= 'pojistenci'),
path('typy-pojisteni/', views.TypPojisteniListView.as_view(), name= 'typy-pojisteni'),
path('pojisteni_list/', views.PojisteniListView.as_view(), name= 'pojisteni_list'),
path('pojistenec/<int:pk>', views.PojistenecDetailView.as_view(), name= 'pojistenec'),
path('pojisteni_detail/<uuid:pk>', views.PojisteniDetailView.as_view(), name= 'pojisteni_detail'),
path('pojistenec/create/', views.PojistenecCreate.as_view(), name='pojistenec_create'),
path('pojistenec/<int:pk>/update/', views.PojistenecUpdate.as_view(), name='pojistenec_update'),
path('pojistenec/<int:pk>/delete/', views.PojistenecDelete.as_view(), name='pojistenec_delete'),
path('pojisteni/create/', views.PojisteniCreate.as_view(), name='pojisteni_create'),
path('pojisteni/<int:pk>/update/', views.PojisteniUpdate.as_view(), name='pojisteni_update'),
path('pojisteni/<int:pk>/delete/', views.PojisteniDelete.as_view(), name='pojisteni_delete'),
path('typ-pojisteni/create/', views.TypPojisteniCreate.as_view(), name='typ-pojisteni_create'),
path('typ-pojisteni/<int:pk>/delete/', views.TypPojisteniDelete.as_view(), name='typ-pojisteni_delete'),
]