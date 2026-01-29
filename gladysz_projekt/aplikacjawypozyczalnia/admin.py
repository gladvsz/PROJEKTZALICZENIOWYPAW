from django.contrib import admin


from .models import Samochod, Marka, ModelAuta, Klient, Wypozyczenie

admin.site.register(Samochod)
admin.site.register(Marka)
admin.site.register(ModelAuta)
admin.site.register(Klient)
admin.site.register(Wypozyczenie)



# Register your models here.
