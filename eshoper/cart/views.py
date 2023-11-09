from django.shortcuts import render, redirect
from .models import Object, CartItem, Kala
from django.contrib import messages
from django.core.paginator import Paginator



def product_list(request):
	products = Object.objects.all()
	return render(request, 'shop.html', {'products': products})

def product_list_page1(request):
	page1 = Kala.objects.all()
	return render(request, 'shop2.html', {'page1': page1})

def number(request):
     items=CartItem.objects.filter(user=request.user)
     total_item = sum(1 * item.quantity for item in items)
     return render(request, 'index.html', {'total_item': total_item})

def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.object.price * item.quantity for item in cart_items)
	return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product_id = Object.objects.get(id=product_id)
    cart_item = CartItem.objects.filter(user=request.user, object=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Cart updated!")
    else:
        CartItem.objects.create(user=request.user, object=product_id)
        messages.success(request, "your Cart updated!")

    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:view_cart")

def home(request):
    return HttpResponse('Hello, World!')

