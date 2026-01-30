from django.urls import path
from . import views

urlpatterns = [


    path('marki_cbv/', views.MarkaList.as_view(), name='marka-list'),
    path('marki_cbv/<int:pk>/', views.MarkaDetail.as_view(), name='marka-detail'),
    
    path('modele-aut_cbv/', views.ModelAutaList.as_view(), name='modelauta-list'),
    path('modele-aut_cbv/<int:pk>/', views.ModelAutaDetail.as_view(), name='modelauta-detail'),
    
    path('klienci_cbv/', views.KlientList.as_view(), name='klient-list'),
    path('klienci_cbv/<int:pk>/', views.KlientDetail.as_view(), name='klient-detail'),
    
    path('samochody_cbv/', views.SamochodList.as_view(), name='samochod-list'),
    path('samochody_cbv/<int:pk>/', views.SamochodDetail.as_view(), name='samochod-detail'),
    
    path('wypozyczenia_cbv/', views.WypozyczenieList.as_view(), name='wypozyczenie-list'),
    path('wypozyczenia_cbv/<int:pk>/', views.WypozyczenieDetail.as_view(), name='wypozyczenie-detail'),

    path('html/klienci/', views.klient_lista_html, name='klient-list-html'),
    path('html/samochody/', views.samochod_lista_html, name='samochod-lista-html'),
]