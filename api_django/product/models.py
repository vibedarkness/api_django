from cgitb import lookup
from itertools import product
from django.db import models

from django.conf import settings

from django.db.models import Q

User= settings.AUTH_USER_MODEL

# Create your models here.

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def rechercheavance(self,query,user=None):
        lookup=Q(name__icontains=query) | Q(content__icontains=query)
        qs=self.filter(lookup)

        if user is not None:
            
            qs=qs.filter(user=user)
            # qs=self.filter(user=user).filter(lookup)
        # qs= (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    
    def rechercheavance(self,query,user=None):
        return self.get_queryset().is_public().rechercheavance()


class Product(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    content=models.TextField()
    price=models.DecimalField(max_digits=15, decimal_places=2)
    public=models.BooleanField(default=True)
    objects=ProductManager()
    @property
    def get_discount(self):

        return "%.2f"%(float(self.price) * 0.5)

    def __str__(self):
        return self.name

