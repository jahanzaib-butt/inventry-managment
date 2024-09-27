from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Dashboard/index.html')

def staff(request):
    return render(request,'Dashboard/staff.html')

def product(request):
    return render(request,'Dashboard/product.html')

def order(request):
    return render(request,'Dashboard/order.html')

