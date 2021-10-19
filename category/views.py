from django.shortcuts import render

def home(req):
    return render(req,'category/home.html')

def category(req):
    return render(req,'category/category.html')

def singleCategory(req,pk):
    pk = pk
    return render(req,'category/single-category.html',{'pk':pk})