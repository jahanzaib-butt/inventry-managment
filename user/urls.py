from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('profile_update/', views.profile_update, name='profile_update'),
]