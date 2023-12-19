from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart, chetout

app_name = 'cart'

urlpatterns = [
    path('AddToCart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cartdetail/', cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('chetout', chetout, name='chetout'),


] 