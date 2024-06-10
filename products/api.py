from . import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as filterr
from django.db.models.aggregates import Count ,Sum,Min,Avg

from rest_framework.permissions import IsAuthenticated

from .pagination import MyPagination

from .models import Product ,Brand,Review ,ProductImages
class ProductFilter(filterr.FilterSet):
    brand = filterr.CharFilter(method='filter_by_brand')

    class Meta:
        model = Product
        fields = ['brand']

    def filter_by_brand(self, queryset, name, value):
        brand_ids = value.split(',')
        return queryset.filter(brand__id__in=brand_ids)

class ProductListAPI(generics.ListAPIView):
    queryset =Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle']
    ordering_fields = ['price']
    pagination_class =MyPagination
    filterset_class = ProductFilter

    # permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.annotate(num_products=Count('product_brand'))
    serializer_class = serializers.BrandListSerializer
    # pagination_class =MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailSerializer




