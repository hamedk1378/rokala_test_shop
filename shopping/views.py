#
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
#
from . import serializers, models



qp_add_products = openapi.Parameter(
    'products',
    in_=openapi.IN_BODY,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_INTEGER)
)

qp_remove_products = openapi.Parameter(
    'products',
    in_=openapi.IN_BODY,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_INTEGER)
)



class ShoppingCartView(APIView):
    serializer_class = serializers.ShoppingCartSerializer

    def get_shopping_cart(self, user):
        shopping_cart, created = models.ShoppingCart.objects.get_or_create(user=user)
        return shopping_cart

    def get(self, request, *args, **kwargs):
        shopping_cart = self.get_shopping_cart(request.user)
        serializer = self.serializer_class(shopping_cart)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, *args, **kwargs):
        shopping_cart = self.get_shopping_cart(request.user)
        serializer = self.serializer_class(shopping_cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializer_class)
    def delete(self, request, *args, **kwargs):
        shopping_cart = self.get_shopping_cart(request.user)
        product_ids = request.data.get('products', [])
        if not product_ids:
            return Response({"detail": "No products provided for removal."}, status=status.HTTP_400_BAD_REQUEST)
        
        products_to_remove = models.Products.objects.filter(id__in=product_ids)
        shopping_cart.products.remove(*products_to_remove)
        serializer = self.serializer_class(shopping_cart)
        return Response(serializer.data, status=status.HTTP_200_OK)