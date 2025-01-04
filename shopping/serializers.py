from rest_framework import serializers

from product_management import models as prod_models
from . import models as shopping_models

class ShoppingCartSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=prod_models.Products.objects.all(),
        many=True
    )

    class Meta:
        model = shopping_models.ShoppingCart
        fields = "__all__"
        read_only_fields = ['user']

    def update(self, instance, validated_data, **kwargs):
        print(kwargs['remove'])
        products = validated_data.pop('products', None)
        if products is not None:
            instance.products.add(*products)
        instance.save()
        return instance