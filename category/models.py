from django.db import models

from category.views import category
import uuid

class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,  editable=False)
    category_name = models.CharField(max_length=200)
    category_description = models.TextField(null=True,blank=True)
    #category_image =
    category_weight = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    packaging_charge = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
    category_vat = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    category_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name