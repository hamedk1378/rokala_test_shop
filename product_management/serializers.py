from rest_framework import serializers

from . import models



class CategoriesCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Categories
        fields= "__all__"


class PriceCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Price
        fields= "__all__"


class ProductsListSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    prices = serializers.SerializerMethodField()

    class Meta:
        model = models.Products
        fields = "__all__"

    def get_categories(self, obj):
        return [category.name for category in obj.categories.all()]

    def get_prices(self, obj):
        prices = obj.price_set.all()
        srlz= PriceCRUDSerializer(prices, many=True)
        return srlz.data
    

class ProductCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Products
        fields= "__all__"