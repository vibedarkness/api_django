from product.models import Product, User

from product.serializer import ProductSerializer
from rest_framework import generics

class SearchListViews(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        qs= super().get_queryset()
        q=self.request.GET.get('q')
        result=Product.objects.none()
       
        if q is not None:
            user=None
            if self.request.user.is_authenticated:
                user=self.request.user
                result=qs.rechercheavance(q,user)
        return result
    