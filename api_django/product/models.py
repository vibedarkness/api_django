from django.db import models

from django.conf import settings

User= settings.AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    content=models.TextField()
    price=models.DecimalField(max_digits=15, decimal_places=2)
    @property
    def get_discount(self):

        return "%.2f"%(float(self.price) * 0.5)

    def __str__(self):
        return self.name

