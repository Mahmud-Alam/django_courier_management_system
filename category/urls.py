from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('branch/', views.branch, name='branch'),
    path('category/', views.category, name='category'),
    path('courier-details/', views.courierDetails, name='courier-details'),
    path('order-form/', views.createOrder, name='order-form'),
    #path('delivery-form/', views.createDelivery, name='delivery-form'),
    path('billing-form/', views.createBilling, name='billing-form'),
]
