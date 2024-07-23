from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.

def search_products(request):
    p=None
    query=""
    if (request.method=="POST"):
        query=request.POST['q']
        if query:
            p=Product.objects.filter(name__icontains=query)
    return render(request,'search_products.html',{'p':p,'query':query})