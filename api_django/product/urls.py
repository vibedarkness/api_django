from django.urls import path

from .views import CreateApiViews, DeleteProductViews,DetailsApiViews, ListeApiViews, ProductMixinsViews, UpdateProductViews


urlpatterns = [
    # path('',api_views_vibe,name='vibe_api'),
      # path('<int:pk>/',DetailsApiViews.as_view()),
      # path('<int:pk>/update',UpdateProductViews.as_view()),
      # path('<int:pk>/delete',DeleteProductViews.as_view()),
      # path('create/',CreateApiViews.as_view()),
      # path('list/',ListeApiViews.as_view()),
      path('create/',ProductMixinsViews.as_view()),
      path('<int:pk>/update',ProductMixinsViews.as_view()),
      path('<int:pk>/delete',ProductMixinsViews.as_view()),
      path('list/',ProductMixinsViews.as_view()),
      path('<int:pk>/detail',ProductMixinsViews.as_view(),name="product_detail"),
      ]
