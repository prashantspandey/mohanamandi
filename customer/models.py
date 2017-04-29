from django.db import models
from django.contrib.auth.models import User

city_choice = (('Jaipur', 'Jaipur'), ('Delhi', 'Delhi'))
state_choice = (('Rajasthan', 'Rajasthan'), ('Delhi', 'Delhi'))


class User_profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    pincode = models.IntegerField()
    city = models.CharField(choices=city_choice, max_length=50)
    state = models.CharField(choices=state_choice, max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
