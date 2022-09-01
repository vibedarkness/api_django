from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer



class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

