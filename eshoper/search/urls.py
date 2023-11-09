from django.urls import include, path
from . import views



urlpatterns = [ 
    path('en/search/', views.SearchResultsView.as_view(), name='search'),
]


