from django.shortcuts import render
from django.http import HttpResponse 

from orders.models import Order

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin   


def list_orders(request):
    orders = Order.objects.all()
    context = {
        "orders" : orders,
    }
    return render(request,"orders/list_orders.html", context=context)

class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list_orders.html'

def create_orders(request):
    Order.objects.create(client= "Andrea", product="Remera Naruto", payment_method="Card")
    return HttpResponse("Orden creada")