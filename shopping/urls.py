from . import views
#
from django.urls import path, include

urlpatterns = [
    path('shopping-cart/', views.ShoppingCartView.as_view(), name='shopping-cart'),
]