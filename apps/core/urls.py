from django.urls import path
from apps.core import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductListApiView.as_view()),
    path('products_shortcut/', views.product_list_with_shortcut),
    # path('products/<int:id>/', views.product_details),
    path('products/<int:id>/', views.ProductDetailApiView.as_view()),
    path('products_shortcut/<int:id>/', views.product_details_with_shortcut),
    path('orders/', views.order_list),
    path('product_info/', views.product_info),
]
