'''
urls.py is created in the my_web_demo directory
'''

from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('men-extra/', views.men_extra, name='men-extra'),
    path('women-extra/', views.women_extra, name='women-extra'),
    path('extra-up-to-50-off/', views.extra_discounts, name='extra-discounts'),
    path('', views.Home, name='home'),
    path('search/', views.search_view, name='search_view'),
    # A page to display all products (for adding to wishlist)
    path('products/', views.product_list_view, name='product_list'),

    # URL to view the wishlist
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    # URL to add an item to the wishlist
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    # URL to view the cart/bag
    path('bag/', views.bag_view, name='bag_view'),
    path('checkout/', views.checkout_view, name='checkout'),
    # URL to move item from wishlist to bag
    path('bag/move-from-wishlist/<int:wishlist_item_id>/', views.move_to_bag, name='move_to_bag'),

    # URL for the user's order history
    path('order-history/', views.order_history, name='order_history'),
    path('account/', views.account_view, name='account'),

    # URL for a single product's detail page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-bag/', views.add_to_bag, name='add_to_bag'),

    re_path(r'^section\.html$', views.section_view, name='section'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # Add other password reset URLs as needed
]
