from decimal import Decimal
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import files

# Create your models here.

# models.py (define your data structure)
# models.py (define your data structure)
# model create for table

class ProductImage(models.Model):
    
    image = models.ImageField(upload_to='images/')
    files = "__all__"
    def __str__(self):
        return self.image


# A basic model for your products
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('women', 'WOMEN'),
        ('men', 'MEN'),
        ('boys', 'BOYS'),
        ('girls', 'GIRLS'),
    ]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="This should be the original price.")
    discount = models.IntegerField(default=0, help_text="Discount percentage (e.g., 20 for 20% off)")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=True, null=True)
    about = models.TextField(blank=True, null=True, help_text="Additional details about the product.")
    description = models.TextField(blank=True, null=True, help_text="Detailed product description.")

    @property
    def original_price(self):
        return self.price

    def get_discounted_price(self):
        if self.discount > 0:
            return (self.price - self.get_discount_amount()).quantize(Decimal('0.01'))
        return self.price.quantize(Decimal('0.01'))

    def get_discount_amount(self):
        if self.discount > 0:
            discount_decimal = Decimal(self.discount) / 100
            return (self.price * discount_decimal).quantize(Decimal('0.01'))
        return Decimal('0.00')

    def __str__(self):
        return self.name

# Model to store items in a user's wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can't add the same product to their wishlist more than once
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.product.name} in {self.user.username}\'s Wishlist'


# Model to store items in a user's shopping bag/cart
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Add fields for product variations like size and color
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} for {self.user.username}'

    # A property to easily calculate the total price for this cart item
    @property
    def unit_price(self):
        return self.product.get_discounted_price()

    @property
    def total_price(self):
        return self.unit_price * self.quantity

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.username


# Model for storing customer orders
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


# Model for storing items within an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)