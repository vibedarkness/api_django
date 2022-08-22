# from dataclasses import fields
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields=('name','content','price','get_discount')

        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'