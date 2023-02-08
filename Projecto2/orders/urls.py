from django.urls import path

from orders.views import list_orders, create_orders
from orders.views import OrdersListView

urlpatterns = [
    path("list-orders", list_orders,),
    path("create-order", create_orders,),
    path('orders-list/', OrdersListView.as_view(), name='list_orders'),
    
]