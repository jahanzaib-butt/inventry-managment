from django.shortcuts import render,redirect
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    user = request.user
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user.username = user.username.lower()
            user.save()
            return redirect('Login')
    context = {'form':form}
    return render(request,'user/register.html',context)

def logout_view(request):
    auth_logout(request)
    return redirect('Login')


def profile(request):
    return render(request,'user/profile.html')

@login_required
def profile_update(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful update
    else:
        form = UpdateUserForm(instance=request.user)
    
    return render(request, 'user/profile_update.html', {'form': form})




