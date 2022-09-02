

from rest_framework import serializers

from rest_framework.reverse import reverse

from .models import Product

from .validators import validate_name


class ProductSerializer(serializers.ModelSerializer):
    # url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name="product_detail",lookup_field="pk")
    email=serializers.EmailField(write_only=True)
    name=serializers.CharField(validators=[validate_name])
    username=serializers.CharField(source="user",read_only=True)
    class Meta:

        model = Product
        fields=('username','email','url','pk','name','content','price','get_discount')

    def create(self,validated_data):
        email=validated_data.pop('email')
        print(email)
        print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name=validated_data.get('name')
        return super().update(instance, validated_data)

    # def validate_name(self,value):
    #     qs=Product.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"le produit {value} existe deja")
    #     return value



    # def get_url(self,obj):
    #     request=self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product_detail",kwargs={'pk':obj.pk},request=request)