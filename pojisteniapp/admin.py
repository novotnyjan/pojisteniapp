from django.contrib import admin

# Register your models here.
from .models import TypPojisteni, Pojistenec, Pojisteni

admin.site.register(Pojisteni)
admin.site.register(Pojistenec)
admin.site.register(TypPojisteni)