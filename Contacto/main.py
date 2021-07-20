from django.core.mail import send_mail, EmailMultiAlternatives
from Contacto import views
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def Enviar_correo(request):
    if request.method=="POST":
        Nombre = request.POST['nombre_completo']
        Telefono = request.POST['telefono']
        Email = request.POST['email']
        Renta = request.POST['renta']
        Prevision = request.POST['prevision']
        Region = request.POST['region']
        Cargas = request.POST['cargas']
        html_content = render_to_string("plantilla_correo.html",{'Nombre':Nombre, 'Telefono':Telefono, 'Email':Email, 'Renta':Renta,'Prevision':Prevision, 'Region':Region, 'Cargas':Cargas})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives("Prueba", text_content, email_from, [recipient_list])
        msg.attach_alternative(html_content,"text/html")
        msg.send



def registrar_clientes(request):
    if request.method=="POST":
        Nombre = request.POST['nombre_completo']
        Telefono = request.POST['telefono']
        Email = request.POST['email']
        Renta = request.POST['renta']
        Prevision = request.POST['prevision']
        Region = request.POST['region']
        Cargas = request.POST['cargas']
        #ins = Clientes(Nombre=Nombre, Telefono=Telefono, Renta=Renta, Prevision=Prevision, Region=Region, Cargas=Cargas, Email=Email)
        #ins.save()
        email_from = settings.EMAIL_HOST_USER
        subject ="Nuevo Contacto de cliente"
        message1 = Nombre + Telefono
        html_content = '<h1>' + Nombre + '</h1><h2>' + Telefono + '</h2><h3>' + Email + '</h3>' 
        recipient_list = "valenzuelaguzmanf@gmail.com"
        msg = EmailMultiAlternatives(subject, message1, email_from, [recipient_list])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        #send_mail(subject, messages,email_from ,['valenzuelaguzmanf@gmail.com'],fail_silently=False)
        print("ha sido guardado en la base de datos")
        return HttpResponse("Ha sido registrado en la base de datos")
    
    return render(request,"index1.html")
