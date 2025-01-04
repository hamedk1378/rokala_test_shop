from django.urls import path, include
from . import views


urlpatterns = [
    path('categories-l/', views.CategoriesListView.as_view(), name= "categories_list"),
    path('categories-c/', views.CategoriesCreateView.as_view(), name= "categories_create"),
    path('categories-rud/<int:pk>/', views.CategoriesUpdateDeleteView.as_view(), name= "categories_update_delete"),
    path('price-l/', views.PriceListView.as_view(), name= "price_list"),
    path('price-c/', views.PriceCreateView.as_view(), name= "price_create"),
    path('price-rud/<int:pk>/', views.PriceUpdateDeleteView.as_view(), name= "price_update_delete"),
    path('products-l/', views.ProductsListView.as_view(), name= "products_list"),
    path('products-c/', views.ProductsCreateView.as_view(), name= "products_create"),
    path('products-rud/<int:pk>/', views.ProductsUpdateDeleteView.as_view(), name= "products_update_delete"),
]