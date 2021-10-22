from django.db import models
from django.db.models.base import Model
from datetime import date
import uuid


class Branch(models.Model):
    branch_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    branch_name = models.CharField(max_length=200, unique=True)
    branch_address = models.TextField(null=True,blank=True, unique=True)
    date_opened = models.DateField(null=True,blank=True)
    branch_revenue = models.DecimalField(max_digits=20, decimal_places=2, null=True,blank=True)
    
    def __str__(self):
        return self.branch_name


class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category_name = models.CharField(max_length=200, unique=True)
    category_description = models.TextField(null=True,blank=True)
    #category_image =
    category_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    packaging_charge = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
    category_vat = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    category_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Order(models.Model):

    GENDER_TYPE = (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )

    order_id = models.CharField(max_length=20, unique=True, primary_key=True, default='Order-')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200, null=True,blank=True, default='+880')
    customer_address = models.TextField(null=True,blank=True)
    customer_gender = models.CharField(max_length=50,choices=GENDER_TYPE, null=True,blank=True)
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    order_date = models.DateField(("Date"), default=date.today)
    recipient_name = models.CharField(max_length=200)
    recipient_phone = models.CharField(max_length=200, null=True,blank=True, default='+880')
    recipient_address = models.TextField(null=True,blank=True)
    recipient_gender = models.CharField(max_length=50,choices=GENDER_TYPE, null=True,blank=True)
    delivery_date  = models.DateField(("Date"), default=date.today)
    
    def __str__(self):
        return self.order_id


class Billing(models.Model):
    billing_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,  editable=False)
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id.order_id

