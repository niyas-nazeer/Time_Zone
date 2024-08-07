from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import products
from .serializers import ProductsSerializer

# products

class productsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = products.objects.all()
    serializer_class = ProductsSerializer

@api_view(['GET', 'POST'])
def products_list(request):
    """
    List all productss, or create a new products.
    """
    if request.method == 'GET':
        products_data = products.objects.all()
        serializer = ProductsSerializer(products_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        product_data = products.objects.get(pk=pk)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(product_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)