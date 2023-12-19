from django.urls import path
from .views import add_to_favorite, favorite_items, remove_from_wishlist

app_name = 'favorite'


urlpatterns = [
    path('<int:product_id>/add', add_to_favorite, name='add_to_favorite'),
    path('wishlist', favorite_items, name='wishlist'),
    path('remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlit'),
    path('remove/', remove_from_wishlist, name='remove_all_wishlit'),




] 
