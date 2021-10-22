from django.db.models.base import Model
from django.forms import ModelForm
from .models import Order, Billing

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        #exclude = ['order_id']

class BillingForm(ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'

