import json

import memcache
from django.core.cache import cache
from django.http import JsonResponse

from django.views.decorators.cache import cache_page

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from clientes.models import Clientes
from clientes.serializers import ClientesSerializer


class ClientesList(APIView):
    serializer_class = ClientesSerializer

    def get(self, request):
        object = cache.get("clientes")

        if object is None:
            clientes = Clientes.objects.all()
            serializer = ClientesSerializer(clientes, many=True)
            cache.set("clientes", serializer.data)
            return JsonResponse(serializer.data, safe=False)


class ClientesCreate(APIView):
    serializer_class = ClientesSerializer

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    @cache_page(60)
    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
