from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.


#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum



from bases.models import ClaseModelo
from inv.models import Pelicula

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




class ComprasEnc(ClaseModelo):
    """Model definition for ComprasEnc."""

    fecha_compra = models.DateField(null=True, blank=True)
    observacion = models.TextField(blank=True,null=True)
    no_factura = models.CharField('Número de Factura', max_length=100)
    fecha_factura = models.DateField('Fecha de facturación')
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)


    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)




    class Meta:
        """Meta definition for ComprasEnc."""

        verbose_name = 'Encabezado de compra'
        verbose_name_plural = 'Encabezado de compras'

    def __str__(self):
        """Unicode representation of ComprasEnc."""
        return self.observacion

    def save(self):
        self.observacion = self.observacion.upper()
        self.total = self.sub_total - self.descuento
        super(ComprasEnc, self).save()


class ComprasDet(ClaseModelo):
    compra = models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)


    def __str__(self):
        return self.producto

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()

    class Meta: 
        verbose_name = 'Detalle de compra'
        verbose_name_plural = 'Detalles de compra'



@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()

    if enc:
        sub_total=ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento=ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total = sub_total["sub_total__sum"]
        enc.descuento = descuento["descuento__sum"]
        enc.save()

    prod = Pelicula.objects.filter(pk=id_producto).first()

    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.id
    fecha_compra = instance.compra.fecha_compra

    prod = Pelicula.objects.filter(pk=id_producto).first()

    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.last_buy = fecha_compra
        prod.save()
