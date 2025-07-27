from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.product_list),
]
