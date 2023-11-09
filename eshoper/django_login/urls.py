from django.urls import include, path
from django.contrib import admin
from .views import register
urlpatterns = [
    path('en/register/', register),
]