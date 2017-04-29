from django.conf.urls import url
from . import views as subscriptionViews

app_name = 'subscription'

urlpatterns = [
    url(r'^$', subscriptionViews.subscription_view, name='subscriptionView'),
    url(r'^confirm_subscription/$', subscriptionViews.confirm_subscription, name='confirm_subscription'),

]
