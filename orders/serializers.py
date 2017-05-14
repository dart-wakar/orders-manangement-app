from rest_framework import serializers
from orders.models import Orders,MyUser
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Orders
        fields = ('id','created','modified','title','website_name','expected_delivery_date','status','delivered_date')

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name',allow_blank=True)
    last_name = serializers.CharField(source='user.last_name',allow_blank=True)
    password = serializers.CharField(source='user.password')
    #orders = serializers.PrimaryKeyRelatedField(many=True,queryset=Orders.objects.all(),null=True,blank=True)

    class Meta:
        model = MyUser
        fields = ('id','username','email','password','first_name','last_name','phone','address')
        write_only_fields = ('password',)

    def update(self,instance,validated_data):
        print("In Update")
        if instance is not None:
            user = User.objects.get(pk=instance.user.pk)
            user = instance.user
            user.username = validated_data.get('user.username',user.username)
            user.email = validated_data.get('user.email',user.email)
            user.password = validated_data.get('user.password',user.password)
            #instance.user.orders = validated_data.get('user.orders',instance.user.orders)
            instance.phone = validated_data.get('phone',instance.phone)
            user.first_name = validated_data.get('user.first_name',user.first_name)
            user.last_name = validated_data.get('user.last_name',user.last_name)
            instance.address = validated_data.get('address',instance.address)
            user.date_joined = validated_data.get('user.date_joined',user.date_joined)
            instance.save()
            return instance

    def create(self,validated_data):
        #user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        #user = User.objects.create(**user_data)
        #print(user)
        print(validated_data)
        user_data = validated_data.pop('user')
        print(user_data)
        user = User.objects.create_user(**user_data)
        user.save()
        myuser = MyUser.objects.create(user=user,**validated_data)
        return myuser
