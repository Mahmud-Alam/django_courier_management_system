from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('branch/', views.branch, name='branch'),
    path('category/', views.category, name='category'),
    path('courier-details/', views.courierDetails, name='courier-details'),
    path('order-form/', views.createOrder, name='order-form'),
    path('update-order-form/<str:pk>/', views.updateOrder, name='update-order-form'),
    path('delete-order-form/<str:pk>/', views.deleteOrder, name='delete-order-form'),
    path('billing-form/', views.createBilling, name='billing-form'),
    path('update-billing-form/<str:pk>/', views.updateBilling, name='update-billing-form'),
]
