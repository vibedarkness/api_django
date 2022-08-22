

from product.models import Product

from django.http import JsonResponse

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ProductSerializer


@api_view(['POST'])
def api_views_vibe(request):
    # dark= Product.objects.all().order_by('?').first()
    # data = {}

    serializer= ProductSerializer(data= request.data)

    if serializer.is_valid(raise_exception=True):

        serializer.save()
        return Response(serializer.data)

    else:
        return Response({'details': 'données invalid'})



    # if dark:
    #     # data= model_to_dict(dark)
    #     # data['name']=dark.name
    #     # data['content']=dark.content
    #     # data['price']=dark.price
    #     data= ProductSerializer(dark).data

