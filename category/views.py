from django.http import request
from django.shortcuts import redirect, render
from .models import Branch, Category, Order, Billing
from .forms import OrderForm, BillingForm
from decimal import Context, Decimal

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
    billing = Billing.objects.all()
    sumAmount=0
    for i in billing:
        sumAmount += i.total_amount
    context = {'order':order,'billing':billing, 'sumAmount':sumAmount}
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


def updateOrder(req, pk):
    order = Order.objects.get(order_id=pk)
    form = OrderForm(instance=order)
    if  req.method=='POST':
        form = OrderForm(req.POST, instance=order)
        if form.is_valid():
            form.save()
            #return redirect('update-billing-form')
            return redirect('update-billing-form',pk)

    context = {'form':form, 'nextId':pk}
    return render(req, 'category/order-form.html',context)

def deleteOrder(req, pk):
    order = Order.objects.get(order_id=pk)
    if  req.method=='POST':
        order.delete()
        return redirect('courier-details')
    context = {'object':order,'nextId':pk}
    return render(req, 'category/delete-order.html',context)


def createBilling(req):
    form = BillingForm()
    currId = 'order-1'
    
    if Order.objects.exists():
        currId = str(Order.objects.latest('order_id'))
    
    category = Order.objects.get(order_id=currId).category_name
    packCharge = category.packaging_charge
    delCharge = category.delivery_charge
    quantity = Order.objects.get(order_id=currId).quantity
    amount = float(packCharge+delCharge)*float(quantity)
    vat = category.category_vat
    total_amount = amount+amount*float(vat)*.01
    #print(packCharge,delCharge,amount,total_amount)

    if  req.method=='POST':
        form = BillingForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('courier-details')

    context = {'form':form,'currId':currId,'packCharge':packCharge*quantity,'delCharge':delCharge*quantity,'quantity':quantity,'amount':amount,'vat':vat,'total_amount':total_amount}
    return render(req, 'category/billing-form.html',context)


def updateBilling(req, pk):
    billing = Billing.objects.get(order_id=pk)
    form = BillingForm(instance=billing)

    category = Order.objects.get(order_id=pk).category_name
    packCharge = category.packaging_charge
    delCharge = category.delivery_charge
    quantity = Order.objects.get(order_id=pk).quantity
    amount = float(packCharge+delCharge)*float(quantity)
    vat = category.category_vat
    total_amount = amount+amount*float(vat)*.01

    if  req.method=='POST':
        form = BillingForm(req.POST, instance=billing)
        if form.is_valid():
            form.save()
            return redirect('courier-details')
    context = {'form':form,'currId':pk,'packCharge':packCharge*quantity,'delCharge':delCharge*quantity,'quantity':quantity,'amount':amount,'vat':vat,'total_amount':total_amount}
    return render(req, 'category/billing-form.html',context)
