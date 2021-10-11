from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from bases.models import ClaseModelo
# Create your views here.

from .models import Categoria, SubCategoria, Productora, Pelicula
from .forms import CategoriaForm, SubCategoriaForm, ProductoraForm, PeliculaForm

class CategoriaView(LoginRequiredMixin, generic.ListView):

    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class CategoriaNew(LoginRequiredMixin, generic.CreateView):

    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)




class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):

    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):

    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')


class SubCategoriaView(LoginRequiredMixin, generic.ListView):

    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'





class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):

    

    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):

    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class =SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)




class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):

    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')





class ProductoraView(LoginRequiredMixin, generic.ListView):

    model = Productora
    template_name = 'inv/productora_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'





class ProductoraNew(LoginRequiredMixin, generic.CreateView):

    

    model = Productora
    template_name = 'inv/productora_form.html'
    context_object_name = 'obj'
    form_class = ProductoraForm
    success_url = reverse_lazy('inv:productora_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class ProductoraEdit(LoginRequiredMixin, generic.UpdateView):

    model = Productora
    template_name = 'inv/productora_form.html'
    context_object_name = 'obj'
    form_class =ProductoraForm
    success_url = reverse_lazy('inv:productora_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


def productora_inactivar(request, id):
    productora = Productora.objects.get(pk=id)
    contexto = {}

    if not productora:
        return redirect('inv:productora_list')

    if request.method == 'GET':
        contexto = {
            'obj': productora
        }

    if request.method == 'POST':
        productora.estado = False
        productora.save()
        return redirect('inv:productora_list')



    return render(request, 'inv/catalogos_del.html', contexto)

    



class PeliculaView(LoginRequiredMixin, generic.ListView):

    model = Pelicula
    template_name = 'inv/pelicula_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'





class PeliculaNew(LoginRequiredMixin, generic.CreateView):

    

    model = Pelicula
    template_name = 'inv/pelicula_form.html'
    context_object_name = 'obj'
    form_class = PeliculaForm
    success_url = reverse_lazy('inv:pelicula_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class PeliculaEdit(LoginRequiredMixin, generic.UpdateView):

    model = Pelicula
    template_name = 'inv/pelicula_form.html'
    context_object_name = 'obj'
    form_class =PeliculaForm
    success_url = reverse_lazy('inv:pelicula_list')
    login_url = 'bases:login'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


def pelicula_inactivar(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    contexto = {}

    if not pelicula:
        return redirect('inv:pelicula_list')

    if request.method == 'GET':
        contexto = {
            'obj': pelicula
        }

    if request.method == 'POST':
        pelicula.estado = False
        pelicula.save()
        return redirect('inv:pelicula_list')



    return render(request, 'inv/catalogos_del.html', contexto)

    





