from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def api_views(request,*args, **kwargs):

    data={
        'name':'omzo',
        'langage':'python', 
    }

    return JsonResponse(data)
