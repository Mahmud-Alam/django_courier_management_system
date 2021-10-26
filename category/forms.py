from django.db.models.base import Model
from django.forms import ModelForm
from .models import Order, Billing

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        #exclude = ['order_id']

    def  __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

class BillingForm(ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
    
    def  __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

