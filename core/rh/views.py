# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from core.rh.models import Unidade, Curso, Aluno, Usuario
from core.rh.forms import PerfilForm
from core.rh.decorators import login_required_custom
from dashboard.forms import RegisterForm, LoginForm
from core.rh.forms import RecoverForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.mail import EmailMessage
import random, string

recover_msg = "Olá {full_name}, \n\
            Nós recebemos seu pedido de redefinição de senha.\n\
            Aqui estpa sua nova senha: {new_password}. \n\
            Obrigado por fazer parte desse projeto. \n\n\
            Social Student."

@login_required
def perfil(request):
	request.session['email'] = request.user.email
	request.session['first_name'] = request.user.first_name
	request.session['last_name'] = request.user.last_name
	try:
		aluno = Aluno.objects.get(email = request.user.email)
		servicos = aluno.servico.all()
		template = loader.get_template('dashboard/index.html')
		context = {
			'servicos': servicos,
		}
	except Exception as e:
		form = PerfilForm
		template = loader.get_template('usuario/profile.html')
		context = {
		    'form': form,
		}

	return HttpResponse(template.render(context, request))

@login_required_custom
def save_perfil(request):
	if request.method == 'POST':
		form = PerfilForm(request.POST, request.FILES)
		unidade = Unidade.objects.get(id = request.POST.get('unidade'))
		curso = Curso.objects.get(id = request.POST.get('curso'))
		if not Aluno.objects.filter(email=request.session["email"]):
			Aluno.objects.create(email=request.session["email"], first_name=request.session["first_name"], last_name=request.session["last_name"], curso=curso, unidade=unidade)
		else:
			aluno = Aluno.objects.get(email=request.session["email"])
			aluno.curso = curso
			aluno.unidade = unidade
			aluno.save()	
		return HttpResponseRedirect("/")

@login_required_custom
def see_perfil(request):
	form = PerfilForm()
	template = loader.get_template('usuario/profile.html')
	context = {
		'form': form,
	}

	return HttpResponse(template.render(context, request))


def recover(request):
	form = RecoverForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			try:
				aluno = Aluno.objects.get(email = request.POST.get('email'))

				new_password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
				aluno.set_password(new_password)
				aluno.save()
				body = recover_msg.format(full_name=aluno.full_name(), new_password=new_password)
				email = EmailMessage('Nova Senha', body, to=[aluno.email])
				email.send()
				# return HttpResponseRedirect("/")
				response_redirect = request.GET.get("next", HttpResponseRedirect("/"))
				return HttpResponse("<script type='text/javascript'>alert('Envinhamos a nova senha para o seu email :D');window.location.href='{}'</script>".format(response_redirect))
			except ValidationError as validationError:
				for field, errors in validationError.message_dict.iteritems():
					form.add_error(field, errors[0])
	return render(request, "registration/login.html", {'form_login': LoginForm(), 'form_register': RegisterForm(), 'form_recover': form})			

def cadastro(request):
	invalid = False
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			try:
				unidade = Unidade.objects.get(id = request.POST.get('unidade'))
				curso = Curso.objects.get(id = request.POST.get('curso'))
				first_name, last_name = request.POST.get('full_name').split(" ")[0], request.POST.get('full_name').split(" ")[-1:][0]
				email = request.POST.get('email')
				senha = request.POST.get('password')
				aluno = Aluno.objects.create(
					first_name = first_name,
					last_name = last_name,
					email = email,
					unidade = unidade,
					curso = curso,
					password = senha, 
					imagem = request._files.get("imagem"))
				
				# return HttpResponseRedirect("/")
				response_redirect = request.GET.get("next", HttpResponseRedirect("/"))
				return HttpResponse("<script type='text/javascript'>alert('Cadastro realizado com sucesso!');window.location.href='{}'</script>".format(response_redirect))

			except ValidationError as validationError:
				for field, errors in validationError.message_dict.iteritems():
					form.add_error(field, errors[0])

	return render(request, "registration/login.html", {'form_login': LoginForm(), 'form_register': form})
# def get_avatar(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     if backend.name == 'facebook':
#         url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
        
#     if backend.name == 'google-oauth2':
#         url = response['image'].get('url')
#         ext = url.split('.')[-1]
#     if url:
#         user.avatar = url
#         user.save()