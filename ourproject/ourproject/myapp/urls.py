# from .models import Product
from django.urls import path
from .views import index, showBrand, showProduct, one_product, oneProductView, filtered_product, ProductView, createOneProductView, deleteOneProductView, updateOneProductView

app_name  = "myapp"

urlpatterns = [
    #normal endpoints
    path("brand/",showBrand,name="showbrand"),
    path("items/",showProduct,name="showproduct"),
    path("filter/",filtered_product,name="filterproducts"),
    path("product/<int:id>/",one_product,name="showoneproduct"),
    path("",index,name="name"),

    #Api endpoints
    path("productView/", ProductView, name="Product_view"),
    path("oneProductView/<int:id>", oneProductView, name="Product_view"),
    path("oneProductView/create/", createOneProductView, name="Product_view"),
    path("updateOneProductView/<int:id>", updateOneProductView, name="Product_view"),
    path("deleteOneProductView/<int:id>", deleteOneProductView, name="Product_view")
    ]