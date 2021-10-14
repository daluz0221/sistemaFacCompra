from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.views import generic

from django.contrib.auth.decorators import login_required, permission_required

from bases.views import Simp
# Create your views here.

from .models import Categoria, SubCategoria, Productora, Pelicula
from .forms import CategoriaForm, SubCategoriaForm, ProductoraForm, PeliculaForm

class CategoriaView(Simp, generic.ListView):

    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    permission_required = 'inv.view_categoria'


class CategoriaNew(SuccessMessageMixin, Simp, generic.CreateView):

    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "Categoria creada satisfactoriamente"
    permission_required = 'inv.add_categoria'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)




class CategoriaEdit(SuccessMessageMixin, Simp, generic.UpdateView):

    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "Categoria actualizada satisfactoriamente"
    permission_required = 'inv.change_categoria'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(Simp, generic.DeleteView):

    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')
    permission_required = 'inv.delete_categoria'


class SubCategoriaView(Simp, generic.ListView):

    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    permission_required = 'inv.view_subcategoria'





class SubCategoriaNew(Simp, generic.CreateView):

    

    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    permission_required = 'inv.add_subcategoria'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class SubCategoriaEdit(Simp, generic.UpdateView):

    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class =SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    permission_required = 'inv.change_subcategoria'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)




class SubCategoriaDel(Simp, generic.DeleteView):

    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')
    permission_required = 'inv.delete_subcategoria'





class ProductoraView(Simp, generic.ListView):

    model = Productora
    template_name = 'inv/productora_list.html'
    context_object_name = 'obj'
    permission_required = 'inv.view_productora'




class ProductoraNew(Simp, generic.CreateView):

    

    model = Productora
    template_name = 'inv/productora_form.html'
    context_object_name = 'obj'
    form_class = ProductoraForm
    success_url = reverse_lazy('inv:productora_list')
    permission_required = 'inv.add_productora'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class ProductoraEdit(Simp, generic.UpdateView):

    model = Productora
    template_name = 'inv/productora_form.html'
    context_object_name = 'obj'
    form_class =ProductoraForm
    success_url = reverse_lazy('inv:productora_list')
    permission_required = 'inv.change_productora'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_productora', login_url='bases:simp')
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
        messages.success(request, 'Productora Inactivada')
        return redirect('inv:productora_list')



    return render(request, 'inv/catalogos_del.html', contexto)

    



class PeliculaView(Simp, generic.ListView):

    model = Pelicula
    template_name = 'inv/pelicula_list.html'
    context_object_name = 'obj'
    permission_required = 'inv.view_pelicula'





class PeliculaNew(Simp, generic.CreateView):

    

    model = Pelicula
    template_name = 'inv/pelicula_form.html'
    context_object_name = 'obj'
    form_class = PeliculaForm
    success_url = reverse_lazy('inv:pelicula_list')
    permission_required = 'inv.add_pelicula'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class PeliculaEdit(Simp, generic.UpdateView):

    model = Pelicula
    template_name = 'inv/pelicula_form.html'
    context_object_name = 'obj'
    form_class =PeliculaForm
    success_url = reverse_lazy('inv:pelicula_list')
    permission_required = 'inv.change_pelicula'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_pelicula', login_url='bases:simp')
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

    





