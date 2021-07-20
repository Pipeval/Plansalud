from django.shortcuts import render
from Contacto.models import Personas, Clientes
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from Plansalud import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def registrar(request):
    if request.method=="POST":
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        ins = Personas(nombre=nombre, telefono=telefono, email=email)
        ins.save()
        return HttpResponse(nombre + " " + telefono + " " + " " +  email + "Ha sido registrado en la base de datos") 
        #print("ha sido guardado en la base de datos")
    
    return render(request,"registro.html")

def registrar_clientes(request):
    if request.method=="POST":
        Nombre = request.POST['nombre_completo']
        Telefono = request.POST['telefono']
        Email = request.POST['email']
        Renta = request.POST['renta']
        Prevision = request.POST['prevision']
        Region = request.POST['region']
        Cargas = request.POST['cargas']
        ins = Clientes(Nombre=Nombre, Telefono=Telefono, Renta=Renta, Prevision=Prevision, Region=Region, Cargas=Cargas, Email=Email)
        ins.save()
        email_from = settings.EMAIL_HOST_USER
        subject ="Nuevo Contacto ingresado a la web"
        recipient_list = "valenzuelaguzmanf@gmail.com"
        html_content = render_to_string("plantilla_correo.html",{'Nombre':Nombre, 'Telefono':Telefono, 'Email':Email, 'Renta':Renta,'Prevision':Prevision, 'Region':Region, 'Cargas':Cargas})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, email_from, [recipient_list])
        msg.attach_alternative(html_content,"text/html")
        msg.send()
        print("ha sido guardado en la base de datos")
        return HttpResponse("Ha sido registrado en la base de datos")
    
    return render(request,"index1.html")



