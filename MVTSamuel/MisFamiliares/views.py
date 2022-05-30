from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar, Yo
from datetime import datetime

# Create your views here.
def MostratFamilia(request):
    Familia_lista = Familiar.objects.all()
    Persona =  Yo.objects.all()
    Fecha = datetime.now()

    return render(request, 'Familia.html', {'fecha': Fecha,'Familia': Familia_lista, 'Persona_1':Persona})

def union_familia(request):
    Familia_lista1 = Familiar.objects.all()

    return render(request, 'Union.html',{'Familia_lista1': Familia_lista1})

def Padre_Familia(request):
    papa = Familiar.objects.all()[0]
    return render(request, 'Padre.html', {'papa': papa})
def Madre_Familia(request):
    mama = Familiar.objects.all()[1]
    return render(request, 'Madre.html', {'mama': mama})
def Hijo_Familia(request):
    bebe = Familiar.objects.all()[2]
    return render(request, 'Hijo.html', {'bebe': bebe})
