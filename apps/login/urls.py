
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.splash, name='splash'),
    url(r'^login_page$', views.login_page, name='login_page'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^create_user$', views.create_user, name='create_user'),
]
