from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', views.CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/del/<int:pk>', views.CategoriaDel.as_view(), name='categoria_del'),

    path('subcategorias/', views.SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', views.SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', views.SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/del/<int:pk>', views.SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('productoras/', views.ProductoraView.as_view(), name='productora_list'),
    path('productoras/new', views.ProductoraNew.as_view(), name='productora_new'),
    path('productoras/edit/<int:pk>', views.ProductoraEdit.as_view(), name='productora_edit'),
    path('productoras/inactivar/<int:id>', views.productora_inactivar, name='productora_inactivar'),

    path('peliculas/', views.PeliculaView.as_view(), name='pelicula_list'),
    path('peliculas/new', views.PeliculaNew.as_view(), name='pelicula_new'),
    path('peliculas/edit/<int:pk>', views.PeliculaEdit.as_view(), name='pelicula_edit'),
    path('peliculas/inactivar/<int:id>', views.pelicula_inactivar, name='pelicula_inactivar'),


]