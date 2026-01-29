from django.contrib import admin


from .models import Samochod, Marka, ModelAuta, Klient, Wypozyczenie

class SamochodAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'rejestracja', 'rok_produkcji']
    list_filter = ['marka']

admin.site.register(Samochod, SamochodAdmin)

class WypozyczenieAdmin(admin.ModelAdmin):
    list_display = ['klient', 'auto', 'data_wypo', 'data_zwrotu']

admin.site.register(Wypozyczenie, WypozyczenieAdmin)

class KlientAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'email']

admin.site.register(Klient, KlientAdmin)

    
admin.site.register(Marka)
admin.site.register(ModelAuta)


# Register your models here.
