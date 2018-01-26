# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^comentar/(?P<id_post>\d+)/(?P<id_servico>\d+)/$', views.comentar, name='comentar'),
]