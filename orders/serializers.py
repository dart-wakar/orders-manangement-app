from rest_framework import serializers
from orders.models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','created','modified','title','website_name','expected_delivery_date','status','delivered_date')
