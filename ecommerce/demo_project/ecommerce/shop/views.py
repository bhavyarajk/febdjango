from django.shortcuts import render,redirect
from  .models import Category,Product
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Shop views

def allcatagories(request):
    item=Category.objects.all()
    return render(request,'catagory.html',{'item':item})

#for displaying products under a particular category
def allproducts(request,pk):
    #p=Product.objects.filter(category__id=pk)

    cate_obj=Category.objects.get(id=pk)
    pro_obj=Product.objects.filter(category=cate_obj)

    return  render(request,'products.html',{'cate_obj':cate_obj,'pro_obj':pro_obj})

def product_details(request,pk):
    product=Product.objects.get(id=pk)
    return  render(request,'product_details.html',{'product':product})

def user_login(request):
    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return allcatagories(request)
        else:
            return HttpResponse("invalid login")
    return render(request,'login.html')

def register(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        cp = request.POST['cp']
        email = request.POST['email']
        f = request.POST['f']
        s= request.POST['s']

        if(cp==password):
            u=User.objects.create_user(username=username,password=password,email=email,first_name=f,last_name=s)
            u.save()
            return user_login(request)
        else:
            return HttpResponse("password are not same")


    return render(request,'register.html')



def user_logout(request):
    logout(request)
    return user_login(request)

