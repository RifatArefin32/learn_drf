from django.urls import path
from apps.core import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductListCreateApiView.as_view()),
    path('products/create/', views.ProductCreateApiView.as_view()),
    path('products_shortcut/', views.product_list_with_shortcut),
    path('products/<int:id>/', views.ProductDetailApiView.as_view()),
    path('products_shortcut/<int:id>/', views.product_details_with_shortcut),
    path('orders/', views.OrderListApiView.as_view()),
    path('product_info/', views.ProductInfoApiView.as_view()),
    path('user-orders/', views.UserOrderListApiView.as_view()),
]
