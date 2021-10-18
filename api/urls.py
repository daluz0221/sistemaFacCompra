from django.urls import path

from . import views

urlpatterns = [
    path("v1/peliculas/", views.PeliculaList.as_view(),name="peli_list"),
    path("v1/peliculas/<str:codigo>", views.PelicualDetalle.as_view(),name="peli_det"),
]