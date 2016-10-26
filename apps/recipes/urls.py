
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.splash, name='splash'),
    url(r'^my_account/$', views.myaccount, name='myaccount'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
]
