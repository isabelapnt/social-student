# -*- coding: utf-8 -*-
from django.conf.urls import url

from core.rh import views

urlpatterns = [
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil_dados/$', views.see_perfil, name='see_perfil'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^recover/$', views.recover, name='recover'),
    url(r'^save/$', views.save_perfil, name='save_perfil'),
]