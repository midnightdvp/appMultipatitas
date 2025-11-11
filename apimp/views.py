from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Adress, Sale 
from .serializers import AdressSerializar, SaleSerializar

""" DIRECCION """

@csrf_exempt
@api_view(['GET','POST'])
def lista_direccion(request):
    if request.method == 'GET':
        direccion = Adress.objects.all()
        serializer = AdressSerializar(direccion,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdressSerializar(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def detalle_direccion(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        direccion = Adress.objects.get(idAdress=data['idAdress'])  
        serializer = AdressSerializar(direccion, data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        direccion = Adress.objects.all()
        direccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
""" VENTA """

@api_view(['GET','POST'])
def lista_venta(request):
    if request.method == 'GET':
        venta = Sale.objects.all()
        serializer = SaleSerializar(venta,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SaleSerializar(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def detalle_venta(request, id_venta):
    try:
        venta = Sale.objects.get(idVenta=id_venta)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SaleSerializar(venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
