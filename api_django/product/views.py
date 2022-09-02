

# from ..api_vibe.permissions import IstaffPermissions
from urllib import request
from product.models import Product

from django.http import JsonResponse

# from django.forms.models import model_to_dict

from rest_framework.response import Response
# from rest_framework.decorators import api_view

from .serializer import ProductSerializer
from api_vibe.mixins import StaffEditorPermissionMixin, UserGetQuerySetProductMixin

from rest_framework import generics, mixins
# , permissions, authentication


class DetailsApiViews(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateApiViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductViews(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductViews(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListeApiViews(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMixinsViews(StaffEditorPermissionMixin,UserGetQuerySetProductMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'
    # authentication_classes=[authentication.SessionAuthentication, authentication.TokenAuthentication]

    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    # permission_classes = [permissions.IsAdminUser, IstaffPermissions]

    def perform_create(self, serializer):
        name=serializer.validated_data.get('name')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content , user=self.request.user)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # def get_queryset(self,*args, **kwargs):
    #     qs=super().get_queryset(*args, **kwargs)
    #     user=self.request.user
    #     return qs.filter(user=user)


# @api_view(['POST'])
# def api_views_vibe(request):
#     # dark= Product.objects.all().order_by('?').first()
#     # data = {}

#     serializer= ProductSerializer(data= request.data)

#     if serializer.is_valid(raise_exception=True):

#         serializer.save()
#         return Response(serializer.data)

#     else:
#         return Response({'details': 'données invalid'})


#     # if dark:
#     #     # data= model_to_dict(dark)
#     #     # data['name']=dark.name
#     #     # data['content']=dark.content
#     #     # data['price']=dark.price
#     #     data= ProductSerializer(dark).data
