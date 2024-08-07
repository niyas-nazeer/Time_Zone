from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import seller
from .serializers import SellerSerializer

# Seller

class SellerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seller to be viewed or edited.
    """
    queryset = seller.objects.all()
    serializer_class = SellerSerializer

@api_view(['GET', 'POST'])
def seller_list(request):
    """
    List all sellers, or create a new seller.
    """
    if request.method == 'GET':
        sellers_data = seller.objects.all()
        serializer = SellerSerializer(sellers_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def seller_detail(request, pk):
    """
    Retrieve, update or delete a seller instance.
    """
    try:
        seller_data = seller.objects.get(pk=pk)
    except seller.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SellerSerializer(seller_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SellerSerializer(seller_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        seller_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)