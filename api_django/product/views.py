

from product.models import Product

from django.http import JsonResponse

from django.forms.models import model_to_dict


def api_views_vibe(request):
    dark= Product.objects.all().order_by('?').first()
    data = {}

    if dark:
        data= model_to_dict(dark)
        # data['name']=dark.name
        # data['content']=dark.content
        # data['price']=dark.price

    return JsonResponse(data)