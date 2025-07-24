from django.core.management.base import BaseCommand
from apps.account.models import User
from apps.core.models import Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Populate dummy core data'

    def handle(self, *args, **kwargs):
        # Create dummy users
        users = []
        user1 = User.objects.create_user(username='user1', email='user1@gmail.com', password='password')
        user2 = User.objects.create_user(username='user2', email='user2@gmail.com', password='password')
        user3 = User.objects.create_user(username='user3', email='user3@gmail.com', password='password')
        users.extend([user1, user2, user3])
        self.stdout.write(self.style.SUCCESS("*** Three users created ***"))

        # Create dummy products
        products = []
        product1 = Product.objects.create(name="Product1", description="Test description 1", price=10.0, stock=5)
        product2 = Product.objects.create(name="Product2", description="Test description 2", price=20.0, stock=15)
        product3 = Product.objects.create(name="Product3", description="Test description 3", price=30.0, stock=35)
        products.extend([product1, product2, product3])
        self.stdout.write(self.style.SUCCESS("*** Five products created ***"))

        # Create dummy orders with order items
        for user in users:
            for _ in range(3):
                order = Order.objects.create(user=user)
                for product in products:
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=2
                    )
        self.stdout.write(self.style.SUCCESS("*** Order items created ***"))