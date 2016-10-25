from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.search, name='search'),
    url(r'^zipsearch$', views.zipsearch, name='zipsearch'),
    url(r'^store$', views.store, name='found'),
]
