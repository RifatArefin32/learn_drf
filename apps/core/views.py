from django.db.models import Max, Min
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.core.models import Product, Order
from apps.core.serializers import ProductSerializer, OrderSerializer, ProducrtInfoSerializer

# List of products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product details
@api_view(['GET'])
def product_details(request, id):
    try:
        product = Product.objects.get(pk=id) 
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Product list with django shortcut
@api_view(['GET'])
def product_list_with_shortcut(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product details with django shortcut
@api_view(['GET'])
def product_details_with_shortcut(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Show all orders
@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# Show product info
@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProducrtInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price'],
        'min_price': products.aggregate(min_price=Min('price'))['min_price']
    })
    return Response(serializer.data, status=status.HTTP_200_OK)