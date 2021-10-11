from django import forms
from django.forms import widgets


from .models import Categoria, SubCategoria, Productora, Pelicula


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la Categoría',
                 'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput}

    
    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': 'Sub Categoría',
                 'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput}

    
    def __init__(self, *args, **kwargs):
        super(SubCategoriaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['categoria'].empty_label = "Seleccione Categoria"


class ProductoraForm(forms.ModelForm):

    class Meta:
        model = Productora
        fields = ['nombre', 'estado']
        labels = {'estado': 'Estado'}
        widget = {'nombre': forms.TextInput}

    
    def __init__(self, *args, **kwargs):
        super(ProductoraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ['codigo','nombre', 'estado', 'description', 'precio', 'existencia', 'last_buy', 'productora', 'subcategoria']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'nombre': forms.TextInput}

    
    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['last_buy'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True


