from django.contrib import admin


from .models import Samochod, Marka, ModelAuta, Klient, Wypozyczenie


class MarkaAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']

admin.site.register(Marka, MarkaAdmin)



class ModelAutaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['marka']

admin.site.register(ModelAuta, ModelAutaAdmin)














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



    



# Register your models here.
