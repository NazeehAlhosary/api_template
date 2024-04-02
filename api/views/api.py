from django.http import JsonResponse
from rest_framework import generics

from ..models import Organization, Product
from ..serializers.products import ProductSerializer

def get_welcome_page(request, *args, **kwargs):
    return JsonResponse({'Message': "Welcome to home page"})


