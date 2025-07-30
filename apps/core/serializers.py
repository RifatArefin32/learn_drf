from rest_framework import serializers
from apps.core.models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'in_stock']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price should be more than zero")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price'
    )
    class Meta:
        model = OrderItem
        fields = [
            'product_name',
            'product_price',
            'quantity',
            'sub_total',
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.sub_total for order_item in order_items)
    
    class Meta:
        model = Order
        fields = [
            'order_id',
            'status',
            'created_at',
            'user',
            'items',
            'total_price',
        ]


class ProducrtInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)