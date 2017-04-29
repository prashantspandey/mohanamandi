from django.conf.urls import url
from . import views as orderViews

app_name = 'veg_order'

urlpatterns = [

    url(r'^$', orderViews.confirm_order, name='confirm_order'),
    url(r'^process_order/$', orderViews.process_order, name='process_order'),

]
