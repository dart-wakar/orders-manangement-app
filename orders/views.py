from orders.models import Orders,MyUser
from orders.serializers import OrderSerializer,UserSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class OrdersList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self,serializer):
        user_id = self.request.user.id
        owner = MyUser.objects.get(pk=user_id)
        serializer.save(owner=owner)

class OrderEdit(APIView):
    def get_order(self,pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        pk = request.data['id']
        order = self.get_order(pk)
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDelete(APIView):
    def get_order(self,pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        pk = request.data['id']
        order = self.get_order(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListRetrieve(APIView):
    def post(self,request,format=None):
        pk_list = request.data['ids']
        if pk_list:
            orders = Orders.objects.filter(pk__in=pk_list)
        else:
            orders = Orders.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

class UserRegister(APIView):
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDelete(APIView):
    def get_myuser(self,pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        pk = request.data['id']
        myuser = self.get_myuser(pk)
        myuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserEdit(APIView):
    def get_myuser(self,pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            print ("oops")
            raise Http404

    def post(self,request,format=None):
        pk = request.data['id']
        myuser = self.get_myuser(pk)
        serializer = UserSerializer(myuser,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
