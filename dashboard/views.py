# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.template import loader
from core.servico.models import Servico

from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_auth, logout as logout_auth
from core.rh.models import Aluno
from core.rh.forms import RecoverForm
from core.servico.models import Servico
from dashboard.forms import RegisterForm, LoginForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from core.rh.decorators import login_required_custom


@login_required_custom
def home(request):
    aluno = Aluno.objects.get(email = request.session["email"])
    servicos = Servico.objects.filter(usuario= aluno)
    template = loader.get_template('dashboard/index.html')
    context = {
        'servicos': servicos,
        'user': aluno
    }
    return HttpResponse(template.render(context, request))

@login_required_custom
def servicos(request):
    aluno = Aluno.objects.get(email = request.session["email"])
    servicos = aluno.unidade.servico_unidade.all().filter(ativo=True)
    template = loader.get_template('dashboard/todos_servicos.html')
    context = {
        'servicos': servicos,
        'user': aluno
    }
    return HttpResponse(template.render(context, request))

@login_required_custom
def participar(request, id_servico):
    servico = Servico.objects.get(id = id_servico)
    aluno = Aluno.objects.get(email = request.session["email"])
    servico.usuario.add(aluno)
    servico.save()

    return HttpResponseRedirect("/servico/posts/" + servico.slug)

@login_required_custom
def settings(request):
    user = request.user
    # try:
    twitter_login = user.social_auth.get(provider='twitter')
    # except UserSocialAuth.DoesNotExist:
    #     twitter_login = None

    # try:
    facebook_login = user.social_auth.get(provider='facebook')
    # except UserSocialAuth.DoesNotExist:
    #     facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'login/settings.html', {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required_custom
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'login/password.html', {'form': form})

def social_login(request):
    if request.user.is_authenticated():
        return HttpResponse(template.render([], request))
    if request.method == 'POST':
            form = LoginForm(request.POST)
            try:
                user = Aluno.objects.get(email=request.POST.get('email'))
                request.session['email'] = user.email
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['imagem'] = user.imagem.url
                request.session['accessed'] = True

                auth_user = authenticate(username=user.username, password=request.POST.get('password'))

                if user and auth_user is not None:
                    return HttpResponseRedirect("/")
                else:
                    form.add_error("email", "Senha ou email incorreto.")
            except ObjectDoesNotExist:
                form.add_error("email", "Não encontramos nenhuma usuário com esse email.")
            
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {'form_login': form, 'form_register': RegisterForm(), 'form_recover':RecoverForm()})
    
def social_logout(request):
    logout_auth(request)
    return HttpResponseRedirect("/")