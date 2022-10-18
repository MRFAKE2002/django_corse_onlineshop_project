from django.urls import path 

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add_to_cart/<int:product_id>', views.product_add_to_cart_view, name='product_add_to_cart'),
    path('remove_from_cart/<int:product_id>', views.product_remove_from_cart_view, name='product_remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]
