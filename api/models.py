from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField

# Create your models here.


class Organization(models.Model):
    id = ShortUUIDField(primary_key=True, unique=True, editable=False, length=8, max_length=8)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8) if self.price is not None else 0  
    
    def get_discount(self):
        return "123"

    def __str__(self):
        return self.name