from django.shortcuts import render
from .models import Branch, Category, Order, Delivery, Billing

def home(req):
    return render(req,'category/home.html')

def branch(req):
    branch = Branch.objects.all()
    context = {'branch':branch}
    return render(req,'category/branch.html',context)

def category(req):
    category = Category.objects.all()
    context = {'category':category}
    return render(req,'category/category.html',context)

def courierDetails(req):
    order = Order.objects.all()
    delivery = Delivery.objects.all()
    billing = Billing.objects.all()
    context = {'order':order,'delivery':delivery,'billing':billing}
    return render(req,'category/courierDetails.html',context)
