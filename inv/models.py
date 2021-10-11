from django.db import models

from bases.models import ClaseModelo



class Categoria(ClaseModelo):

    descripcion = models.CharField('Descripción de la categoría', max_length=100, unique=True)

    
    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'
        


class SubCategoria(ClaseModelo):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción de la categoría', max_length=100)


    def __str__(self):
        return '{}-{}'.format(self.categoria.descripcion, self.descripcion)


    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria', 'descripcion')


class Productora(ClaseModelo):

    nombre = models.CharField('Empresa productora', max_length=100, unique=True)


    def __str__(self):
        return '{}'.format(self.nombre)


    def save(self):
        self.nombre = self.nombre.upper()
        super(Productora, self).save()

    class Meta:
        verbose_name_plural = 'Productoras'


class Pelicula(ClaseModelo):

    codigo = models.CharField('Código de pelicula', max_length=50, unique=True)
    nombre = models.CharField('Nombre de la película', max_length=80)
    description = models.CharField('descripción', max_length=500)
    precio = models.FloatField(default=0)
    existencia = models.PositiveIntegerField(default=1)
    last_buy = models.DateField('Última compra', null=True, blank=True)

    productora = models.ForeignKey(Productora, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre

    def save(self):
        self.nombre = self.nombre.upper()
        super(Pelicula, self).save()


    class Meta:
        verbose_name_plural = 'Películas'
        unique_together = ('codigo', )
