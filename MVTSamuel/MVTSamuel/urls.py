"""MVTSamuel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from MisFamiliares.views import MostratFamilia, Padre_Familia, Madre_Familia, Hijo_Familia
from MisFamiliares.views import union_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familia/', MostratFamilia),
    path('Union/', union_familia),
    path('papa/', Padre_Familia),
    path('mama/', Madre_Familia),
    path('bebe/', Hijo_Familia)
]
