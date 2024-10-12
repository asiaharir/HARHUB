from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cotegory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    category = models.ForeignKey(Cotegory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return f"{self.user.username}'s Cart"
    
    @property
    
    def total_price(self):
        return self.product.price * self.quantity
    
class Cartitem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cart.user.username}-{self.product.name}'
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    
class promotion (models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.title
 
    
    
    
    
    
    