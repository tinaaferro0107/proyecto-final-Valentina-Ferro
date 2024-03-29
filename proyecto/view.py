
from django.http import HttpResponse
from django.shortcuts import render
from app.models import *

def home(request,):
    return render (request,"index.html")

def inicio(request):
    return HttpResponse(f"Bienvenido")
def medicos(request):
    return HttpResponse(f"Bienvenido")
def pacientes(request):
    return HttpResponse(f"Bienvenido")
def obras_sociales(request):
    return HttpResponse(f"Bienvenido")
def receta(request):
    return HttpResponse(f"Bienvenido")
    