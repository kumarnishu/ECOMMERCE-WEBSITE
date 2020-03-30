from app.models import Cart,Order
from django.shortcuts import  render,redirect

def cart(request):
    if request.user.is_active:
        cart_items = Cart.objects.all().filter(customer=request.user)
    else:
        cart_items = Cart.objects.all()
    c = len(cart_items)
    if request.user.is_active:
        order_items = Order.objects.all().filter(customer=request.user)
    else:
        order_items = Order.objects.all()
    o = len(order_items)
    cs=0
    for i in cart_items:
        cs+=float(i.product.price)
    os=0
    for i in order_items:
        os+=float(i.product.price)
    order_items = Order.objects.filter(customer=request.user)
    cart_items = Cart.objects.filter(customer=request.user)

    context = {
    'cart':cart_items,
    'orders':order_items,
    'c': c,
    'o': o,
    'cs':cs,
    'os':os,
    }
    return context;


