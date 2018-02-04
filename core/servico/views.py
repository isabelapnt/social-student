# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.detail import DetailView
from core.servico.models import Servico
from django.shortcuts import render, render_to_response, get_object_or_404
from core.post.forms import PostForm
from core.servico.forms import ServicoForm
from core.rh.decorators import login_required_custom
from core.rh.models import Aluno
from core.post.models import Post
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from core.tag.models import Tags
# Create your views here.

class ServicoDetailView(DetailView):

    model = Servico

    def get_object(self):
        obj = get_object_or_404(Servico, slug=self.kwargs['slug'])
        return obj

    def get_context_data(self, **kwargs):
        context = super(ServicoDetailView, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        # # context['now'] = timezone.now()
        return context    


@login_required_custom
def novo_post(request, id_servico):
	if request.method == 'POST':	
		servico = Servico.objects.get(id = id_servico)
		user = Aluno.objects.get(email=request.session["email"])
		titulo = request.POST.get('titulo')
		conteudo = request.POST.get('conteudo')

		post = Post.objects.create(
			servico = servico,
			criado_por = user,
			titulo = titulo,
			conteudo = conteudo
			)


	return HttpResponseRedirect("/servico/posts/"+ servico.slug)

@login_required_custom
def criar_servico(request):
	user = Aluno.objects.get(email=request.session["email"])
	form = ServicoForm()
	tags = Tags.objects.all()
	template = loader.get_template('servico/criar_servico.html')
	context = {
		'form' :  form,
		'tags' :  tags,
		'user':   user
	}

	return HttpResponse(template.render(context, request))

@login_required_custom
def leave_servico(request, id_servico):
	servico = Servico.objects.get(id = id_servico)
	aluno = Aluno.objects.get(email = request.session["email"])
	servico.usuario.remove(aluno)
	servico.save()
	return HttpResponseRedirect("/")

@login_required_custom
def save_servico(request):
	if request.method == 'POST':	
		tags = request.POST.get('tag')
		carrosel = True if request.POST.get('carrosel') == "true" else False
		anexo = True if request.POST.get('anexo') == "true" else False
		nome = request.POST.get('nome')
		resumo = request.POST.get('resumo')
		user = Aluno.objects.get(email=request.session["email"])

		servico = Servico.objects.create(
			nome = nome,
			criado_por = user.full_name(),
			resumo = resumo,
			has_carrosel = carrosel,
			has_anexo = anexo,
			unidade = user.unidade
			)
		servico.usuario.add(user)
		servico.save()

		for id_tag in tags:
			tag = Tags.objects.get(id = int(id_tag))
			servico.tag.add(tag)
			servico.save()


	response_redirect = request.GET.get("next", HttpResponseRedirect("/"))
	return HttpResponse("<script type='text/javascript'>alert('O Serviço foi encaminhado para moderação, em breve você receberá um retorno :D');window.location.href='{}'</script>".format(response_redirect))
