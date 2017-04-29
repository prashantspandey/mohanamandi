from django.db import models


class Vegetable(models.Model):
    veg = 'Vegetable'
    fruit = 'Fruit'
    type_choice = ((veg, 'Vegetable'), (fruit, 'Fruit'))
    name = models.CharField(max_length=100)
    pricekg = models.IntegerField()
    subpricekg = models.IntegerField()
    organic = models.BooleanField(default=False)
    photo = models.URLField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=50, choices=type_choice)

    def __str__(self):
        return self.name
