from django.template import Template, context
from django.http import HttpResponse

def saludar(request):
    saludo = "Bienbenido al proyecto con django"
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    saludo = f"Bienbenido al proyecto {nombre} en {apellido}"
    return HttpResponse(saludo)