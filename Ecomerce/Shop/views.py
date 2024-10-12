from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Product, Cart, Cartitem, Cotegory

def product_list(request):
    products = Product.objects.all()
    lproducts = Product.objects.order_by('-id')[:3]
    categories = Cotegory.objects.all()
    cart_items_count = count_cart_items(request)        
    return render(request, 'Product/product_list.html', {'products': products, 'categories': categories, 'cart_items_count': cart_items_count, 'lproducts': lproducts})

def category_products(request, category_id):
    category = get_object_or_404(Cotegory, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'Product/category_products.html', {'category': category, 'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = Cartitem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.total_price for item in cart_items)
    return render(request, 'Product/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cartitem, id=cart_item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

def count_cart_items(request):
    try:
        cart = Cart.objects.get(user=request.user)
        return cart.cartitem_set.aggregate(total_items=Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0
    
def mobiles_view(request):
    category = get_object_or_404(Cotegory, name='mobiles')
    cart_items_count = count_cart_items(request)
    products = Product.objects.filter(category=category)
    return render(request, 'Product/mobiles.html', {'products': products, 'cart_items_count': cart_items_count})

def computers_view(request):       
    products = Product.objects.filter(category__name='computers')
    cart_items_count = count_cart_items(request)
    return render(request, 'Product/computers.html', {'products': products, 'cart_items_count': cart_items_count})

def Airphone_view(request):
    products = Product.objects.filter(category__name='Airphone')
    cart_items_count = count_cart_items(request)
    return render(request, 'Product/Airphone.html', {'products': products, 'cart_items_count': cart_items_count})

def Remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart= Cart.objects.get_or_create(user=request.user)
    
    cartitem= Cartitem.objects.get(cart=cart, product=product)
    
    cartitem.delete()
    return redirect('cart_view')



def Bixi_lacagta(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart= Cart.objects.get_or_create(user=request.user)
    
    cartitem =  Cartitem.objects.get_or_create(cart=cart, product=product)
    
    cartitem.delete()
    return redirect('cart_view')
# ... existing code ...




