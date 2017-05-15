from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User,related_name='user')
    phone = models.CharField(max_length=15,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    #@receiver(post_save, sender = User)
    #def create_profile_for_user(sender, instance = None, created = False, **kwargs):
    #    if created:
    #        MyUser.objects.get_or_create(user = instance)

    #@receiver(pre_delete, sender = User)
    #def delete_profile_for_user(sender, instance = None, **kwargs):
    #    if instance:
    #        user_profile = MyUser.objects.get(user = instance)
    #        user_profile.delete()

class Orders(models.Model):
    owner = models.ForeignKey(MyUser,related_name='orders',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100,blank=True)
    website_name = models.CharField(max_length=100,blank=True)
    expected_delivery_date = models.DateField(blank=True,null=True)
    status = models.IntegerField(default=0)
    delivered_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        ordering = ('created',)
