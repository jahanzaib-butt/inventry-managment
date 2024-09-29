from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff_details/<int:pk>/',views.staff_details,name='dashboard-staff-details'),
    path('product/',views.product,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
    path('product_delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product_update/<int:pk>/',views.product_update,name='dashboard-product-update'),
]
