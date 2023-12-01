from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)
from decimal import Decimal

def checkout(request):
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = Decimal(request.POST["price"])
        request.session.setdefault('quantity_sum', 0)
        request.session.setdefault('price_sum', 0)

        request.session['total_charge'] = float(quantity_from_form * price_from_form)
        order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=request.session['total_charge'])
        
        all_orders = Order.objects.all()
        for order in all_orders:
            request.session['quantity_sum'] += order.quantity_ordered
            request.session['price_sum'] += float(order.total_price)

    return redirect('/amadon/display')

        

def display(request):                        
    return render(request, "store/checkout.html",)

def destroySession(request):
    if request.method == "POST":
        if ('quantity_sum' in request.session) or  ('price_sum' in request.session):
            del request.session['quantity_sum']
            del request.session['price_sum']
    return redirect('/')
  