from django.db.models import Max, Min
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.models import Product, Order
from apps.core.serializers import ProductSerializer, OrderSerializer, ProducrtInfoSerializer

# List of products
# Function based view
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Class based view
class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        min_stock = self.request.query_params.get('min_stock')

        if min_price:
            queryset = queryset.filter(price__gte = min_price)
        if max_price:
            queryset = queryset.filter(price__lte = max_price)
        if min_stock:
            queryset = queryset.filter(stock__gte = min_stock)
        
        return queryset


# Create product api view
class ProductCreateApiView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

# Create product list create api view
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


# Product details
# Function based view
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

# Class based view
class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = []


# Product list with django shortcut
# Function based view
@api_view(['GET'])
def product_list_with_shortcut(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Product details with django shortcut
# Function based view
@api_view(['GET'])
def product_details_with_shortcut(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Show all orders
# Function based view
@api_view(["GET"])
def order_list(request):
    orders = Order.objects.prefetch_related('items', 'items__product').all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# Class based view
class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items', 'items__product').all()
    serializer_class = OrderSerializer


# Show product info
# Function based view
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

# class based view
class ProductInfoApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProducrtInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price'],
            'min_price': products.aggregate(min_price=Min('price'))['min_price']
        })
        return Response(serializer.data, status=status.HTTP_200_OK)



# User order list
# Class based view
class UserOrderListApiView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items', 'items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)