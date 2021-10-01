from .models import  Product
from rest_framework import serializers

class ProductViewSet(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

