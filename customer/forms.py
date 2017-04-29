from django.contrib.auth.models import User
from .models import User_profile
from .models import city_choice, state_choice
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address_line1 = forms.CharField(max_length=100)
    address_line2 = forms.CharField(max_length=100)
    pincode = forms.IntegerField()
    city = forms.ChoiceField(choices=city_choice)
    state = forms.ChoiceField(choices=state_choice)
