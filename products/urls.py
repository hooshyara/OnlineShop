from django.urls import path
from .views import product_list, product_detail, search_product,add_product, delete_product, update_product, add_category, category_list
app_name = 'products'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('result/<str:category>', product_list, name='product_category'),
    path('<int:pk>', product_detail, name='product_detail'),
    path('search', search_product, name='search_product'),
    path('add_product', add_product, name='add_product'),
    path('add_category', add_category, name='add_category'),

    path('<int:pk>/delete', delete_product, name='delete_product'),
    path('<int:pk>/update', update_product, name='update_product'),
    # path('product_filter_view', product_filter_view, name='product_filter_view'),
    path('category_list', category_list, name='category_list'),





 


    

] 