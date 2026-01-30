from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Marka, ModelAuta, Klient, Samochod, Wypozyczenie
from .serializers import ( MarkaSerializer, ModelAutaSerializer, KlientSerializer, SamochodSerializer, WypozyczenieSerializer)
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

class MarkaList(ListCreateAPIView):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MarkaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

class KlientList(ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    permission_classes = [IsAdminUser]

class KlientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

class SamochodList(ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SamochodDetail(RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ModelAutaList(ListCreateAPIView):
    queryset = ModelAuta.objects.all()
    serializer_class = ModelAutaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ModelAutaDetail(RetrieveUpdateDestroyAPIView):
    queryset = ModelAuta.objects.all()
    serializer_class = ModelAutaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WypozyczenieList(ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

class WypozyczenieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]



def klient_lista_html(request):
    klienci = Klient.objects.all()
    return render(request, "aplikacjawypozyczalnia/klienci_lista.html", {'klienci': klienci})    


def samochod_lista_html(request):
    marka_id = request.GET.get('marka')
    if marka_id:
        samochody = Samochod.objects.filter(model__marka_id=marka_id)
    else:
        samochody = Samochod.objects.all()
        
    return render(request, "aplikacjawypozyczalnia/samochody_lista.html", {'samochody': samochody})