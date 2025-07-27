from rest_framework import serializers
from apps.core.models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'in_stock']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price should be more than zero")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity'
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            'order_id',
            'status',
            'created_at',
            'user',
            'items',
        ]