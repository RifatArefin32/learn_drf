from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.product_list),
    path('products_shortcut/', views.product_list_with_shortcut),
    path('products/<int:id>/', views.product_details),
]
