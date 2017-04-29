from django.db import models
from django.contrib.auth.models import User
from vegetables.models import Vegetable
from vegetableOrder.models import Vegetable_order


class Subscription(models.Model):
    subscription_type = (('Silver', 'Silver'), ('Gold', 'Gold'),
                         ('Platinum', 'Platinum'))
    subscriber = models.OneToOneField(User)
    sub_type = models.CharField(max_length=50, choices=subscription_type)
    cost = models.IntegerField()
    moneyLeft = models.IntegerField()
    dateStarted = models.DateTimeField(auto_now_add=True, auto_now=False)
    length = models.IntegerField()

    def __str__(self):
        return self.subscriber.username + " " + self.sub_type


class Subscription_VegetableList(models.Model):
    sub = models.ForeignKey(Subscription, blank=True, null=True)
    order = models.ForeignKey(Vegetable_order, blank=True, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=3)
    discount = models.DecimalField(default=5.0, decimal_places=1, max_digits=3)
