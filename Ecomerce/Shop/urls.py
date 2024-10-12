from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('mobiles/', views.mobiles_view, name='mobiles'), 
    path('computers/', views.computers_view, name='computers'), 
    path('Airphone/', views.Airphone_view, name='Airphone'), 
    path('Remove_from_cart/<int:product_id>/', views.Remove_from_cart, name='Remove_from_cart'), 
    path('Bixi_lacagta/<int:product_id>/', views.Bixi_lacagta, name='Bixi_lacagta'), 
]