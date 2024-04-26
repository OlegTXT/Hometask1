from django.urls import path
from shop.views import *

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category-detail/<int:pk>/', Category_detail.as_view(), name='category_detail'),
    path('add-card/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
