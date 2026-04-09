from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Profile model (extra user information ke liye)
class Profile(models.Model):

    # Django default user se connect
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Signup form ka Full Name
    full_name = models.CharField(max_length=100)

    # Email (optional because already User me hota hai, but safe)
    email = models.EmailField()

    # Account create date
    created_at = models.DateTimeField(auto_now_add=True)


    # Admin panel me name show hoga
    def __str__(self):
        return self.full_name
    

class Logo(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.name
    
# This file defines database tables


# Brand Model
class Brand(models.Model):
    # Name of cosmetic brand
    name = models.CharField(max_length=100)

    # Brand image
    image = models.ImageField(upload_to='brand_images/')

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):

    # Each product belongs to a brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    # Product name
    name = models.CharField(max_length=200)

    # Product price
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Product description
    description = models.TextField()

    # Product image
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name