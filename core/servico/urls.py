# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
from core.servico.views import ServicoDetailView

urlpatterns = [
    url(r'^posts/(?P<slug>[-\w]+)/$', ServicoDetailView.as_view(), name='servico_slug'),
    url(r'^novo_post/(?P<id_servico>\d+)/$', views.novo_post, name='novo_post'),
    url(r'^criar_servico/$', views.criar_servico, name='criar_servico'),
    url(r'^save_servico/$', views.save_servico, name='save_servico'),
    url(r'^deixar_servico/(?P<id_servico>\d+)/$', views.leave_servico, name='leave_servico'),

]