"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('storeapp.urls_user')),
    path('produse/', include('storeapp.urls')),
    path('producator/', include('storeapp.urls1')),
    path('categorie/', include('storeapp.urls2')),
    path('furnizor/', include('storeapp.urls3')),
    path('comanda/', include('storeapp.urls4')),
    path('vanzari/', include('storeapp.urls5')),
    path('job/', include('storeapp.urls6')),
    path('angajat/', include('storeapp.urls7')),
    path('', include('storeapp.urls_main')),
]
