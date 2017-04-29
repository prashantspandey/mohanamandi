from django.conf.urls import url

from . import views as customerview
app_name = 'customer'

urlpatterns = [
    url(r'^register/$', customerview.UserFormView.as_view(), name='register'),
    url(r'^$', customerview.user_login, name='login'),
    url(r'^logout/$', customerview.user_logo, name='logout'),
]
