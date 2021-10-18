from rest_framework.views import APIView
from rest_framework.response import Response


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q

from inv.models import Pelicula

from .serializers import PeliculaSerializer


# Create your views here.


class PeliculaList(APIView):
    def get(self, request):
        prod = Pelicula.objects.all()
        data = PeliculaSerializer(prod, many=True).data
        return Response(data)


class PelicualDetalle(APIView):

    def get(self, request, codigo):

        prod = get_object_or_404(Pelicula,Q(codigo=codigo)|Q(nombre=codigo))
        data = PeliculaSerializer(prod).data
        return Response(data)


