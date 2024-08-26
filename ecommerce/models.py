from django.db import models


from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoryImage = models.ImageField(upload_to ='category -images/')
    new = models.BooleanField(default=True)
    features = models.TextField()
    includes = models.TextField(default=list)

    def __str__(self):
         return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    categoryImage = models.ImageField(upload_to='category -images/')

    def __str__(self):
        return self.name



class Cart(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_per_unit = 10

    def calculate_total_price(self):
        self.total_price = self.quantity * self.price

    def save(self, *args, **kwargs):
        self.calculate_total_price()
        super().save(*args, **kwargs)




class CartItem(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)


