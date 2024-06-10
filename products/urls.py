from django.urls import path
from .views import ProductList ,ProductDetail ,BrandDetail,BrandList , mydebug,add_review
from . import api
urlpatterns = [
    path("debug", mydebug),
    path("brands", BrandList.as_view()),
    path("brands/<slug:slug>", BrandDetail.as_view()),
    path('' ,ProductList.as_view() ),
    path('<slug:slug>' ,ProductDetail.as_view() ),
    path('<slug:slug>/add-review' ,add_review ),


    #api 
    path('api/products' ,api.ProductListAPI.as_view() ),
    path('api/products/<int:pk>' ,api.ProductDetailAPI.as_view() ),
   
    path('api/brands' ,api.BrandListAPI.as_view() ),
    path('api/brands/<int:pk>' ,api.BrandDetailAPI.as_view() ),
   
]
