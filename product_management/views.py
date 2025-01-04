#
from rest_framework import generics, permissions

#
from . import models, serializers

#
from django.db.models import Q

#
from accounts.permissions import IsAdminUserOrReadOnly

#
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


qp_category_name = openapi.Parameter(
    'category_name',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Category's name"
)
qp_price_min = openapi.Parameter(
    'price_min',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_NUMBER,
    description="Category's name"
)
qp_price_max = openapi.Parameter(
    'price_max',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_NUMBER,
    description="Category's name"
)
qp_price_region = openapi.Parameter(
    'price_region',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Category's name"
)
qp_prod_name = openapi.Parameter(
    'prod_name',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Category's name"
)
qp_prod_is_tech = openapi.Parameter(
    'prod_is_tech',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Category's name"
)
qp_prod_color = openapi.Parameter(
    'prod_color',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="Category's name"
)


class CategoriesListView(generics.ListAPIView):
    serializer_class= serializers.CategoriesCRUDSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        c_name = self.request.query_params.get('category_name')
        if c_name:
            return models.Categories.objects.filter(name= c_name)
        return models.Categories.objects.all()
    
    @swagger_auto_schema(manual_parameters=[qp_category_name])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoriesCreateView(generics.CreateAPIView):
    serializer_class= serializers.CategoriesCRUDSerializer
    queryset= models.Categories.objects.all()
    permission_classes= [IsAdminUserOrReadOnly & permissions.DjangoModelPermissions]


class CategoriesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= serializers.CategoriesCRUDSerializer
    queryset= models.Categories.objects.all()
    permission_classes= [IsAdminUserOrReadOnly & permissions.DjangoModelPermissions]


class PriceListView(generics.ListAPIView):
    serializer_class= serializers.PriceCRUDSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        queryset = models.Price.objects.all()

        amount_min = self.request.query_params.get('price_min')
        amount_max = self.request.query_params.get('price_max')
        region = self.request.query_params.get('price_region')

        filters = Q()
        if amount_min:
            filters &= Q(amount__gte=amount_min)
        if amount_max:
            filters &= Q(amount__lte=amount_max)
        if region:
            filters &= Q(region__iexact=region)

        return queryset.filter(filters)
    
    @swagger_auto_schema(manual_parameters= [qp_price_min, qp_price_max, qp_price_region])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PriceCreateView(generics.CreateAPIView):
    serializer_class= serializers.PriceCRUDSerializer
    queryset= models.Price.objects.all()
    permission_classes= [IsAdminUserOrReadOnly and permissions.DjangoModelPermissions]


class PriceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= serializers.PriceCRUDSerializer
    queryset= models.Price.objects.all()
    permission_classes= [IsAdminUserOrReadOnly and permissions.DjangoModelPermissions]


class ProductsListView(generics.ListAPIView):
    serializer_class= serializers.ProductsListSerializer
    queryset= models.Products.objects.all()
    permission_classes= [permissions.AllowAny]


class ProductsListView(generics.ListAPIView):
    serializer_class = serializers.ProductsListSerializer
    queryset = models.Products.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        prod_name = self.request.query_params.get('prod_name')
        prod_is_tech = self.request.query_params.get('prod_is_tech')
        prod_color = self.request.query_params.get('prod_color')

        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        price_region = self.request.query_params.get('price_region')

        category_name = self.request.query_params.get('category_name')

        filters = Q()
        if prod_name:
            filters &= Q(name__icontains=prod_name)
        if prod_is_tech is not None:
            filters &= Q(is_tech=(prod_is_tech.lower() == 'true'))
        if prod_color:
            filters &= Q(color__iexact=prod_color)

        if price_min:
            filters &= Q(price__amount__gte=price_min)
        if price_max:
            filters &= Q(price__amount__lte=price_max)
        if price_region:
            filters &= Q(price__region__iexact=price_region)

        if category_name:
            filters &= Q(categories__name__icontains=category_name)

        return queryset.filter(filters).prefetch_related('categories', 'price_set').distinct()

    @swagger_auto_schema(manual_parameters= 
                            [
                                qp_price_min, qp_price_max, qp_price_region,
                                qp_category_name, qp_prod_name, qp_prod_is_tech, qp_prod_color
                            ]
                        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductsCreateView(generics.CreateAPIView):
    serializer_class= serializers.ProductCRUDSerializer
    queryset= models.Products.objects.all()
    permission_classes= [IsAdminUserOrReadOnly & permissions.DjangoModelPermissions]


class ProductsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Products.objects.all()
    permission_classes= [IsAdminUserOrReadOnly & permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return serializers.ProductsListSerializer
        else:
            return serializers.ProductCRUDSerializer
