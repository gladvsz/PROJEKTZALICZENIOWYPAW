from django.contrib import admin


from .models import Samochod, Marka, ModelAuta

admin.site.register(Samochod)
admin.site.register(Marka)
admin.site.register(ModelAuta)


# Register your models here.
