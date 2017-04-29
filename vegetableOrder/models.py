from django.db import models
from django.contrib.auth.models import User
from vegetables.models import Vegetable
from cart.models import Cart
from django.utils import timezone


class Vegetable_order(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=200)
    total = models.IntegerField()
    moneySaved = models.IntegerField()
    orderdate = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username + " at: " + str(self.orderdate)[:10]
