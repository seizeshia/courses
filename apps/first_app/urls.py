from django.conf.urls import url
from . import views

urlpatters=[
    url(r'^$', views.index),
    url(r'^adding$', views.adding),
    url(r'^removing$', views.removing)
]
