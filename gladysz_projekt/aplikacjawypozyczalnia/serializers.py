from rest_framework import serializers
from .models import Marka, ModelAuta, Klient, Samochod, Wypozyczenie
from datetime import date

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['id', 'nazwa']
        read_only_fields = ['id']

    def validate_nazwa(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa marki musi zaczynać się z wielkiej litery")
        return value 


class ModelAutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAuta
        fields = ['id', 'marka', 'nazwa']
        read_only_fields = ['id']

    def validate_nazwa(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa modelu musi zaczynać się od wielkiej litery!")
        return value        
    

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'imie', 'nazwisko', 'email']
        read_only_fields = ['id']

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Imie może zawierać tylko litery!") 

        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa modelu musi zaczynać się od wielkiej litery!")
        return value   
    
    def validate_nazwisko(self, value):
        if not value.replace('-', '').isalpha():
            raise serializers.ValidationError("Nazwisko może zawierać tylko litery!")
            
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwisko musi zaczynać się od wielkiej litery!")
            
        return value
    

class SamochodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samochod
        fields = [
            'id', 'marka', 'model', 'rok_produkcji', 'rejestracja', 
            'vin', 'napęd', 'paliwo', 'przekładnia', 'moc', 'pojemnosc'
        ]
        read_only_fields = ['id']

    def validate_vin(self, value):
        if len(value) != 17:
            raise serializers.ValidationError("Numer VIN musi mieć dokładnie 17 znaków!")
        return value.upper()

    def validate_moc(self, value):
        if value <= 0:
            raise serializers.ValidationError("Moc musi być liczbą dodatnią!")
        return value

    def validate_pojemnosc(self, value):
        if value <= 0:
            raise serializers.ValidationError("Pojemność musi być liczbą dodatnią!")
        return value

    def validate_rok_produkcji(self, value):
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(f"Rok produkcji nie może być z przyszłości ({current_year})!")
        if value < 1990:
            raise serializers.ValidationError("Rok produkcji nie może być starszy niż 1990!")
        return value



class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = ['id', 'auto', 'klient', 'data_wypo', 'data_zwrotu']
        read_only_fields = ['id']

    def validate_data_wypo(self, value):
        if value < date.today():
            raise serializers.ValidationError("Nie można wypożyczyć auta z datą wsteczną!")
        return value


    def validate(self, data):
        start = data.get('data_wypo')
        end = data.get('data_zwrotu')

        if start and end and start > end:
            raise serializers.ValidationError({
                "data_zwrotu": "Data zwrotu nie może być wcześniejsza niż data wypożyczenia!"
            })
        
        return data