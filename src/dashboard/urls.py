# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^servicos/$', views.servicos, name='servicos'),
    url(r'^participar/(?P<id_servico>\d+)/$', views.participar, name='participar'),
    url(r'^social/login/$', views.social_login, name='social_login'),
    url(r'^social/logout/$', views.social_logout, name='social_logout'),
]