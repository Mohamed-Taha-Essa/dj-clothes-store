#form 
from rest_framework import serializers
from .models import Product,Brand,Review ,ProductImages
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model =Review 
        fields = ['user' , 'content' ,'rate' ,'created_at']

class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model =ProductImages 
        fields = ['image']

class ProductListSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()
    class Meta:
        model = Product
        # fields ='__all__'
        fields =['name','brand','price','review_count', 'avg_rate','tags','image']
            
    
class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields ='__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandDetailSerializer()
    images = ProductImagesSerializers(source ='product_image' ,many = True)
    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields=['name','price','review_count', 'avg_rate',
          'flag' , 'subtitle' ,'description', 'quantity','brand','tags','images']

class BrandListSerializer(serializers.ModelSerializer):
    num_products = serializers.IntegerField(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'num_products']  # Include other fields as needed





