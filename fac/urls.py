from django.urls import path

from . import views, reportes

urlpatterns = [
   
   path('clientes/', views.ClienteView.as_view(), name='cliente_list'),
   path('clientes/new', views.ClienteNew.as_view(), name='cliente_new'),
   path('clientes/<int:pk>', views.ClienteEdit.as_view(), name='cliente_edit'),
   path('cliente/estado/<int:id>', views.cliente_inactivar, name='cliente_inactivar'),


   path('facturas/', views.FacturaView.as_view(), name="factura_list"),
   path('facturas/new', views.facturas, name="factura_new"),
   path('facturas/edit/<int:id>', views.facturas, name="factura_edit"),


   path('facturas/buscar-producto', views.PeliculaView.as_view(), name="factura_peli"),
   path('facturas/borrar-detalle/<int:id>', views.borrar_detalle_factura, name="factura_borrar_det"),


   path('facturas/imprimir/<int:id>', reportes.factura_recibo_imprimir, name="factura_imprimir_one"),
   path('facturas/imprimir-todas/<str:f1>/<str:f2>', reportes.imprimir_factura_list, name="factura_imprimir_all"),
   
]