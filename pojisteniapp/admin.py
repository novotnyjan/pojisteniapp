from django.contrib import admin

# Register your models here.
from .models import Pojisteni, Pojistenec, PojisteniInstance

admin.site.register(PojisteniInstance)
admin.site.register(Pojistenec)
admin.site.register(Pojisteni)