from django.http import HttpResponse
from django.shortcuts import render
from AppCafe.models import VariedadCafe,VariedadTe,VariedadGaseosa

def VariedadCafe(request):

    variedadcafe = VariedadCafe (nombre=" ", marca=" ", precio=" ")
    variedadcafe.save()
    pedido = f"VariedadCafe: {variedadcafe.nombre} VariedadCafe: {variedadcafe.marca} VariedadCafe: {variedadcafe.procedencia} VariedadCafe: {variedadcafe.precio}"

    return HttpResponse(pedido)

def inicio(request):

    return render(request, "AppCafe/inicio.html")

def variedadcafe(request):

    return render(request, "AppCafe/variedadcafe.html")

def formcafe(request):

    return render(request, "AppCafe/formcafe.html")

from AppCafe.forms import Pedido