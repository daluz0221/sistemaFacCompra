from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
import datetime

from django.db.models import Sum

# Create your views here.

from bases.views import Simp
from inv.models import Pelicula

from .models import Proveedor, ComprasDet, ComprasEnc
from .forms import ComprasEncForm, ProveedorForm

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


class ComprasView(Simp, generic.ListView):
    
    model = ComprasEnc
    template_name = 'cmp/compras_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_comprasenc'


@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:simp')
def compras(request, compra_id=None):

    peli = Pelicula.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            print(enc)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura':fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }

            form_compras = ComprasEncForm(e)
        else:
            det = None
        

        contexto = {
            'pelicula': peli,
            'encabezado': enc,
            'detalle': det,
            'form_enc': form_compras
        }
       

    if request.method == 'POST':
        fecha_compra = request.POST.get("fecha_compra")
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = request.POST.get("proveedor")
        sub_total = 0
        descuento = 0
        total = 0

        if not compra_id:
            prov = Proveedor.objects.get(pk=proveedor)

            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,                   
                proveedor = prov,
                uc = request.user
            )

            if enc:
                enc.save()
                compra_id = enc.id
        else:
            enc = ComprasEnc.objects.filter(pk=compra_id).first()

            if enc:
                enc.fecha_compra=fecha_compra
                enc.observacion=observacion
                enc.no_factura=no_factura
                enc.fecha_factura=fecha_factura
                enc.um = request.user.id
                enc.save()

        if not compra_id:
            return redirect('cmp:compras_list')


        pelicula = request.POST.get("id_id_pelicula")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle = request.POST.get("id_descuento_detalle")
        total_detalle = request.POST.get("id_total_detalle")

        peli = Pelicula.objects.get(pk=pelicula)

        det = ComprasDet(
            compra=enc,
            producto=peli,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            
            costo=0,
            uc = request.user
        )

        if det:
            det.save()

            sub_total=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()

        return redirect('cmp:compras_edit', compra_id=compra_id)

    return render(request, 'cmp/compras.html', contexto)




class ComprasDetDelete(Simp, generic.DeleteView):
    permission_required = "cmp.delete_comprasdet"
    model = ComprasDet
    template_name = "cmp/compras_det_del.html"
    context_object_name = 'obj'


    def get_success_url(self):
        compra_id=self.kwargs['compra_id']
        return reverse_lazy('cmp:compras_edit', kwargs={'compra_id':compra_id})
            