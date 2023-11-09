from django.urls import include, path
from django.contrib import admin
from . import views

app_name = 'paginator'

urlpatterns = [
    path('en/shop/', views.list_creates, name='list_creates'),
    path('en/sabad/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('home', views.home, name='home'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('en/result/', views.SearchResultsView.as_view(), name='result'),
]