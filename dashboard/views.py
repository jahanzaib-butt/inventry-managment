from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='Login')
def index(request):
    return render(request,'Dashboard/index.html')

@login_required(login_url='Login')
def staff(request):
    return render(request,'Dashboard/staff.html')

@login_required(login_url='Login')
def product(request):
    return render(request,'Dashboard/product.html')

@login_required(login_url='Login')
def order(request):
    return render(request,'Dashboard/order.html')

