from django.urls import path
from products.views import  ProductListCreateView , reviews_view, ProductDetaliUpdateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name="products"),
    path('products/<int:pk>/', ProductDetaliUpdateView.as_view(), name='product'),
    path('reviews/', reviews_view, name="reviews")
]