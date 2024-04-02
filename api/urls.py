from django.urls import path
from .views.api import get_welcome_page
from .views.product import *

urlpatterns = [
    path("", get_welcome_page, name="APIWelcomePage"),
    path('product/<str:pk>/', ProductDetailAPIView.as_view()),
    path('product/<str:pk>/update/', product_update_view),
    path('product/<str:pk>/delete/', ProductDetailAPIView.as_view()),
    path('products/', product_list_create_view),
]