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
    first_name = serializers.CharField(source='user.first_name',allow_blank=True,allow_null=True)
    last_name = serializers.CharField(source='user.last_name',allow_blank=True,allow_null=True)
    password = serializers.CharField(source='user.password')
    orders = serializers.PrimaryKeyRelatedField(many=True,queryset=Orders.objects.all(),allow_null=True,required=False)

    class Meta:
        model = MyUser
        fields = ('id','username','email','password','first_name','last_name','phone','address','orders')
        write_only_fields = ('password',)

    def update(self,instance,validated_data):
        print("In Update")
        if instance is not None:
            print("Instance is not null")
            #user = User.objects.get(pk=instance.user.pk)
            print(instance.user.first_name)
            print(validated_data)
            new_user_data = validated_data.pop('user')
            print(new_user_data)
            instance.user.username = new_user_data['username']
            instance.user.email = new_user_data['email']
            instance.user.password = new_user_data['password']
            instance.user.first_name = new_user_data['first_name']
            instance.user.last_name = new_user_data['last_name']
            instance.user.username = validated_data.get('user.username',instance.user.username)
            instance.user.email = validated_data.get('user.email',instance.user.email)
            instance.user.password = validated_data.get('user.password',instance.user.password)
            #instance.user.orders = validated_data.get('user.orders',instance.user.orders)
            instance.phone = validated_data.get('phone',instance.phone)
            instance.user.first_name = validated_data.get('user.first_name',instance.user.first_name)
            instance.user.last_name = validated_data.get('user.last_name',instance.user.last_name)
            instance.address = validated_data.get('address',instance.address)
            instance.user.date_joined = validated_data.get('user.date_joined',instance.user.date_joined)
            #print(instance.user.first_name)
            #new_user_data = validated_data.pop('user')
            #print(new_user_data)
            #print(validated_data.pop('user'))
            instance.user.save()
            instance.save()
            return instance

    def create(self,validated_data):
        #user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        #user = User.objects.create(**user_data)
        #print(user)
        print("Inside create")
        print(validated_data)
        user_data = validated_data.pop('user')
        print(user_data)
        user = User.objects.create_user(**user_data)
        user.save()
        myuser = MyUser.objects.create(user=user,**validated_data)
        myuser.save()
        return myuser
