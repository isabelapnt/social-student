# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.rh.decorators import login_required_custom
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from core.post.models import Post
from core.comentario.models import Comentario
from core.rh.models import Aluno
from core.servico.models import Servico
# from core.rh.models import Aluno
# Create your views here.

@login_required_custom
def comentar(request, id_post, id_servico):
	if request.method == 'POST':	
		servico = Servico.objects.get(id = id_servico)
		post = Post.objects.get(id = id_post)
		descricao = request.POST.get('descricao')
		user = Aluno.objects.get(email=request.session["email"])
		Comentario.objects.create(
			usuario = user,
			descricao = descricao,
			post = post)
		

	return HttpResponseRedirect("/servico/posts/"+ servico.slug)