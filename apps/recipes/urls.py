from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^init$', views.first_time, name='first'),
    url(r'^create$', views.create, name='create'),
    url(r'^new$', views.new, name='new'),

]
