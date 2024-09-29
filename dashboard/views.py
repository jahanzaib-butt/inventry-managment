from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url='Login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    staff_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'products': products,
        'form': form,
        'orders_count': orders_count,
        'product_count': product_count,
        'staff_count': staff_count
    }
    return render(request, 'Dashboard/index.html', context)

@login_required(login_url='Login')
def staff(request):
    staffs = User.objects.all()
    staff_count = staffs.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context = {'staffs':staffs, 'staff_count':staff_count, 'orders_count':orders_count, 'product_count':product_count}
    return render(request,'Dashboard/staff.html',context)

@login_required(login_url='Login')
def staff_details(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'Dashboard/staff_details.html',context)

@login_required(login_url='Login')
def product(request):
    products = Product.objects.all()
    product_count = products.count()
    orders_count = Order.objects.all().count()
    staff_count = User.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'products':products, 'form':form, 'product_count':product_count,
        'orders_count':orders_count, 'staff_count':staff_count
        }
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
    orders = Order.objects.all()
    orders_count = orders.count()
    product_count = Product.objects.all().count()
    staff_count = User.objects.all().count()
    context = {
        'orders':orders, 'orders_count':orders_count, 'product_count':product_count,
        'staff_count':staff_count
        }
    return render(request,'Dashboard/order.html',context)