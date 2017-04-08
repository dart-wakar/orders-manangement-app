from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Orders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100,blank=True)
    website_name = models.CharField(max_length=100,blank=True)
    expected_delivery_date = models.DateField(blank=True)
    status = models.IntegerField(default=0)
    delivered_date = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('created',)
