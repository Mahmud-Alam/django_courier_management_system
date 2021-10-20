from django.http import request
from django.shortcuts import redirect, render
from .models import Branch, Category, Order, Delivery, Billing
from .forms import OrderForm, DeliveryForm, BillingForm
from decimal import Decimal

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

def createOrder(req):
    form = OrderForm()
    nextId = 'ord-1'
    if Order.objects.exists():
        nextId = 'ord-'+str(int(str(Order.objects.latest('order_id')).split("-")[-1])+1)   
    #print(nextId,type(nextId))

    if  req.method=='POST':   
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('billing-form')

    context = {'form':form,'nextId':nextId}
    return render(req, 'category/order-form.html',context)

"""
def createDelivery(req):
    form = DeliveryForm()
    currId = 'ord-1'
    if Order.objects.exists():
        currId = str(Order.objects.latest('order_id'))   

    if  req.method=='POST':   
        form = DeliveryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('billing-form')

    context = {'form':form,'currId':currId}
    return render(req, 'category/delivery-form.html',context)

def createBilling(req):
    form = BillingForm()
    currId = 'ord-1'
    
    if Order.objects.exists():
        currId = str(Order.objects.latest('order_id'))
    
    category = Order.objects.get(order_id=currId).category_name
    packCharge = category.packaging_charge
    delCharge = category.delivery_charge
    quantity = Order.objects.get(order_id=currId).quantity
    amount = float(packCharge+delCharge)*float(quantity)
    vat = category.category_vat
    total_amount = amount+amount*float(vat)*.01
    
    if  req.method=='POST':
        form = BillingForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,'currId':currId,'packCharge':packCharge*quantity,'delCharge':delCharge*quantity,'quantity':quantity,'amount':amount,'vat':vat,'total_amount':total_amount}
    return render(req, 'category/billing-form.html',context)

"""

def createBilling(req):
    form1 = DeliveryForm()
    form2 = BillingForm()
    currId = 'ord-1'
    
    if Order.objects.exists():
        currId = str(Order.objects.latest('order_id'))
    
    category = Order.objects.get(order_id=currId).category_name
    packCharge = category.packaging_charge
    delCharge = category.delivery_charge
    quantity = Order.objects.get(order_id=currId).quantity
    amount = float(packCharge+delCharge)*float(quantity)
    vat = category.category_vat
    total_amount = amount+amount*float(vat)*.01
    
    if  req.method=='POST':
        form1 = DeliveryForm(req.POST)
        form2 = BillingForm(req.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/')

    context = {'form1':form1,'form2':form2,'currId':currId,'packCharge':packCharge*quantity,'delCharge':delCharge*quantity,'quantity':quantity,'amount':amount,'vat':vat,'total_amount':total_amount}
    return render(req, 'category/billing-form.html',context)
