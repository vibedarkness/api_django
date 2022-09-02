from itertools import product
from multiprocessing import context
from rest_framework import serializers


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product_detail", lookup_field="pk")
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()



class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    number=serializers.CharField(read_only=True)
    user_product=serializers.SerializerMethodField(read_only=True)

    def get_user_product(self, obj):
        user = obj
        product = user.product_set.all()
        request=self.context.get("request")

        return ProductInlineSerializer(product, many=True,context={'request':request}).data
