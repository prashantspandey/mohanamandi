from django.conf.urls import url
from . import views

app_name = 'vegetables'

urlpatterns = [
    url(r'^$', views.vegetable_view, name='vegetable_view'),

]
