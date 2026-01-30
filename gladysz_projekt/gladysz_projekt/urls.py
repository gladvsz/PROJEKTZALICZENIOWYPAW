"""
URL configuration for gladysz_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from aplikacjawypozyczalnia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('aplikacjawypozyczalnia.urls')),

    path('html/klienci/', views.klient_lista_html, name='klient-lista-html'),
    path('html/samochody/', views.samochod_lista_html, name='samochod-lista-html'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
