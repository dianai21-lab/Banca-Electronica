from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def ingreso(request):
    if request.method == "POST":
        if request.POST['usuario'] != "" and request.POST['contrasena'] != "":
            nuevoUsuario = Usuario.objects.create(usuario=request.POST['usuario'] , contraseña=request.POST['contrasena'])
            return redirect('activacion', usuario=nuevoUsuario.pk)
        else:
            return redirect('activacion', usuario=6)
    else:
        return render(request, "ingresobe.html")

def activacion(request, usuario=None):
    if request.method == "POST":
        DatosPersonales.objects.create(usuario=Usuario.objects.get(pk= request.POST['usuario']) , identificacion=request.POST['identificacion'],
                                       nombres=request.POST['nombre'] , cuenta=request.POST['numeroCuenta'],
                                       correo=request.POST['correo'] , telefono=request.POST['telefono'])
        return render(request, "activacion.html" )
    else:
        return render(request, "activacion.html" , {'idUsuario': usuario})