from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
#import Contacto.models import Clientes



def index(request): #primera vista
    
    return render(request,"index.html")


def registrar_contacto(request):
    if request.method=="POST":
        Nombre = request.POST['nombre_completo']
        Telefono = request.POST['telefono']
        Email = request.POST['email']
        Renta = request.POST['renta']
        Prevision = request.POST['prevision']
        Region = request.POST['region']
        Cargas = request.POST['cargas']
        #ins = Clientes(Nombre = Nombre, Telefono=Telefono, Email=Email, Renta = Renta, Prevision=Prevision, Region = Region, Cargas=Cargas)
        #ins.save()
        print("ha sido guardado en la base de datos")
        return HttpResponse("Ha sido registrado en la base de datos") 
        
    
    return render(request,"registro.html")

