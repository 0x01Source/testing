from django.db import models
from django.contrib.auth.models import User

# Add the necessary models for product management here
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add more fields as needed for product management