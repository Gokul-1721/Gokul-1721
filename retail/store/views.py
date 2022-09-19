from pickle import GET
from django.shortcuts import render
from .serializers import ProductSerializer,CategorySerializer

from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/product-list/',
        'Detail View':'/product-detail/<int:id>/',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>/',
        'Delete':'/product-delete/<int:id>/',

    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    products=Product.objects.get(id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    products=Product.objects.get(id=pk)
    serializer=ProductSerializer(instance=products,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request,pk):
    products=Product.objects.get(id=pk)
    products.delete()
    return Response('Item delete successfully')


def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html',{'products':products})
