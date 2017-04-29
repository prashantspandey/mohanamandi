from django.conf.urls import url
from . import views as cartViews

app_name = 'cart'

urlpatterns = [
    url(r'^$', cartViews.cart, name='cart'),

]
