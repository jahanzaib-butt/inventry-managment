from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    user = request.user
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user.username = user.username.lower()
            user.save()
            return redirect('dashboard-index')
    context = {'form':form}
    return render(request,'user/register.html',context)

def logout_view(request):
    auth_logout(request)
    return redirect('Login')


def profile(request):
    return render(request,'user/profile.html')


