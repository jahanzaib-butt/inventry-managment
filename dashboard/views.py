from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
# Create your views here.
@login_required(login_url='Login')
def index(request):
    return render(request,'Dashboard/index.html')

@login_required(login_url='Login')
def staff(request):
    return render(request,'Dashboard/staff.html')

@login_required(login_url='Login')
def product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {'products':products, 'form':form}
    return render(request,'Dashboard/product.html',context)

@login_required(login_url='Login')
def product_delete(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard-product')
    context = {'product':product}
    return render(request,'Dashboard/product_delete.html',context)

@login_required(login_url='Login')
def product_update(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form =ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=product)
    context = {'form':form}
    return render(request,'Dashboard/product_update.html',context)

@login_required(login_url='Login')
def order(request):
    return render(request,'Dashboard/order.html')

