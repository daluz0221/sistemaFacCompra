from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
import json



# Create your views here.

from bases.views import Simp

from .models import Proveedor
from .forms import ProveedorForm

class ProveedorView(Simp, generic.ListView):

    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_proveedora'

class ProveedorNew(Simp, generic.CreateView):
    
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    permission_required = 'cmp.add_proveedora'


    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)


class ProveedorEdit(Simp, generic.UpdateView):
    
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    permission_required = 'cmp.change_proveedora'


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)



@login_required(login_url='/login/')
@permission_required('cmp.change_proveedor', login_url='bases:simp')
def proveedor_inactivar(request, id):

    prv = Proveedor.objects.filter(pk=id).first()
    contexto = {}

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':prv}

    if request.method == 'POST':
        prv.estado = False
        prv.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request, 'cmp/inactivar_prv.html', contexto)


