from django.db import models
from django.contrib.auth.models import User
from vegetables.models import Vegetable


class Cart(models.Model):
    carter = models.ForeignKey(User)
    veg = models.ForeignKey(Vegetable, blank=True, null=True)
    total = models.IntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.carter.username + " " + self.veg.name
