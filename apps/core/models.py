import uuid
from django.db import models
from apps.account.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending"
        CONFIRMED = "Confirmed"
        CANCELLED = "Cancelled"

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4) 
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    
    def __str__(self):
        return f"Ordered {self.order_id} by {self.user.first_name} {self.user.last_name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def sub_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in order no. {self.order.order_id}" 