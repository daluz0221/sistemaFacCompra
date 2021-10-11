from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class ClaseModelo(models.Model):


    estado = models.BooleanField(default=True)
    fc = models.DateTimeField('Fecha creado', auto_now_add=True)
    fm = models.DateTimeField('fecha modificado', auto_now=True, auto_now_add=False)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.PositiveIntegerField(null=True, blank=True)


    class Meta:
        abstract = True




