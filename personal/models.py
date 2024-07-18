from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.usuario}"
 

class DatosPersonales(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    cuenta = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.usuario.usuario} - {self.nombres}"
 