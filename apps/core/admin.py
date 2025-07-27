from django.contrib import admin
from apps.core.models import OrderItem, Order, Product

# Register Order with related OrderItem model
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

# Register Product Model
admin.site.register(Product)