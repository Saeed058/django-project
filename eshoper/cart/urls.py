from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('en/shop/', views.product_list, name='product_list'),
    path('en/shop/shop2/', views.product_list_page1, name='product_list_page1'),
	# path('en/', views.number, name='number'),
	path('home', views.home, name='home'),
	path('en/cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
