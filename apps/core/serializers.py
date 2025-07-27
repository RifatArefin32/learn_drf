from rest_framework import serializers
from apps.core.models import Product

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'in_stock']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price should be more than zero")
        return value