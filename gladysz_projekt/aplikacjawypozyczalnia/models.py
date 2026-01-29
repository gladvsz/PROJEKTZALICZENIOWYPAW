from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Przekladnia(models.IntegerChoices):
    M = 1, 'Manual'
    A = 2, 'Automat'

class Paliwo(models.IntegerChoices):
    ON = 1, 'Diesel'
    PB = 2, 'Benzyna'
    EL = 3, 'Elektryczny'
    HY = 4, 'Hybrydowy'


class Naped(models.IntegerChoices):
    FWD = 1, 'Na przednie koła'
    RWD = 2, 'Na tylne koła'
    AWD = 3, '4x4'

class Marka(models.Model):
    nazwa = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Marka" 
        verbose_name_plural = "Marki"  
        ordering = ['nazwa']

class ModelAuta(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, verbose_name="Marka", null=True)
    nazwa = models.CharField(max_length=50, unique=True, verbose_name="Nazwa modelu") 

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Model" 
        verbose_name_plural = "Modele"  

         


class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "Klienci"
        ordering = ['nazwisko']
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Samochod(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.PROTECT, verbose_name="Marka",)
    model = models.ForeignKey(ModelAuta, on_delete=models.PROTECT, verbose_name="Model",)   

    rok_produkcji = models.PositiveIntegerField(
        validators= [MinValueValidator(1990), MaxValueValidator(2026)],
        default=2024,
        verbose_name="Rok Prokukcji"
    
    )

    napęd = models.IntegerField(choices=Naped.choices, default=Naped.FWD)   
    paliwo = models.IntegerField(choices=Paliwo.choices, default=Paliwo.PB) 
    przekładnia = models.IntegerField(choices=Przekladnia, default=Przekladnia.M)
    moc = models.PositiveIntegerField(verbose_name="Moc (KM)", null=True)
    pojemnosc = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Pojemność (cm3)", null=True)
    przyspieszenie = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="0-100 km/h (s)", null=True)
    rejestracja = models.CharField(max_length=10, unique=True, null=True)
    vin = models.CharField(max_length=17, unique=True, null=True)
    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return f"{self.marka} {self.model}"
    

class Wypozyczenie(models.Model):
        auto = models.ForeignKey(Samochod, on_delete=models.CASCADE)
        klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
        data_wypo = models.DateField()
        data_zwrotu = models.DateField()

        class Meta:
            verbose_name_plural = "Wypożyczenia"
            ordering = ['data_wypo']

        def __str__(self):
            return f"Wynajem: {self.auto} dla {self.klient}"    