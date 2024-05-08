

from django.urls import path
from .views import ProductListCreateView, ProductRetrieveView, ProductUpdateView, ProductDestroyView,CategoryListCreateView, CategoryRetrieveView, CategoryUpdateView,CategoryDestroyView,CartListCreateView, CartRetrieveView, CartUpdateView, CartDestroyView, CartItemListCreateView, CartItemRetrieveView, CartItemUpdateView, CartItemDestroyView



# urlpatterns = [
#     path('products/', ProductAPIView.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),

#     path('categories/', CategoryAPIView.as_view(), name='category-list'),
#     path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),

#     path('carts/', CartAPIView.as_view(), name='cart-list'),
#     path('carts/<int:pk>/', CartAPIView.as_view(), name='cart-detail'),

#     path('carts-items/', CartItemAPIView.as_view(), name='cart-item-list'),
#      path('cart-items/<int:pk>/', CartItemAPIView.as_view(), name='cartitem-detail'),
    
# ]

urlpatterns = [
    path('products', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveView.as_view(), name='product-retrieve'),
    path('update_products/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('delete_products/<int:pk>/', ProductDestroyView.as_view(), name='product-delete'),

    path('categories', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category-retrieve'),
    path('update_categories/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('delete_categories/<int:pk>/', CategoryDestroyView.as_view(), name='category-delete'),

    path('cart', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartRetrieveView.as_view(), name='cart-retrieve'),
    path('update_cart/<int:pk>/', CartUpdateView.as_view(), name='cart-update'),
    path('delete_cart/<int:pk>/', CartDestroyView.as_view(), name='cart-delete'),

    path('cart-item', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('cart-item/<int:pk>/', CartItemRetrieveView.as_view(), name='cart-retrieve'),
    path('update-cart-item/<int:pk>/', CartItemUpdateView.as_view(), name='cart-update'),
    path('delete-cart-item/<int:pk>/', CartItemDestroyView.as_view(), name='cart-delete'),

]

