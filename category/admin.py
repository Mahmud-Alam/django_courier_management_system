from django.contrib import admin
from .models import Branch, Category, Order, Billing

admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Billing)
