
from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset


router=DefaultRouter()

router.register('product-b',ProductViewset,basename='product-a')

urlpatterns= router.urls