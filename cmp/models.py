from django.db import models

# Create your models here.

from bases.models import ClaseModelo

class Proveedor(ClaseModelo):
    
    descripcion = models.CharField('Nombre del proveedor', max_length=100, unique=True)
    direccion = models.CharField('Dirección', max_length=250, null=True, blank=True)
    contacto = models.CharField('Contacto', max_length=100)
    telefono = models.CharField('Teléfono', max_length=20)
    email = models.CharField('Correo electrónico', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = 'Proveedores'





