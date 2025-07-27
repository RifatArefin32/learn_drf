from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.core.models import Product
from apps.core.serializers import ProductSerailizer

# List of products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerailizer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product details
@api_view(['GET'])
def product_details(request, id):
    try:
        product = Product.objects.get(pk=id) 
        serializer = ProductSerailizer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def product_list_with_shortcut(request):
    products = get_list_or_404(Product)
    serializer = ProductSerailizer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)