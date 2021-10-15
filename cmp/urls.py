from django.urls import path

from . import views
from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path('proveedor/', views.ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new', views.ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', views.ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', views.proveedor_inactivar, name='proveedor_inactivar'),
    
    
    
     
    path('compras/', views.ComprasView.as_view(), name='compras_list'),
    path('compras/new', views.compras, name='compras_new'),
    path('compras/edit/<int:compra_id>', views.compras, name='compras_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>', views.ComprasDetDelete.as_view(), name='compras_del'),

    path('compras/listado', reporte_compras, name="compras_print_all"),
    path('compras/<int:compra_id>/imprimir', imprimir_compra, name="compras_print_one"),
   
]