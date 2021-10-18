from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


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



class ClaseModelo2(models.Model):


    estado = models.BooleanField(default=True)
    fc = models.DateTimeField('Fecha creado', auto_now_add=True)
    fm = models.DateTimeField('fecha modificado', auto_now=True, auto_now_add=False)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.PositiveIntegerField(null=True, blank=True)
    uc = UserForeignKey(auto_user_add=True, related_name='+')
    um = UserForeignKey(auto_user=True, related_name='+')


    class Meta:
        abstract = True



