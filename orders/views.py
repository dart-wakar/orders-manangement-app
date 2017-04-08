from orders.models import Orders
from orders.serializers import OrderSerializer
from rest_framework import generics

# Create your views here.

class OrdersList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
