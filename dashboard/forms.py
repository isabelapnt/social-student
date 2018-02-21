# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from core.rh.models import Aluno, Unidade, Curso, Usuario

class RegisterForm(forms.Form):
    model = Aluno

    fields = [
            'email',
            'first_name',
            'last_name',
            'unidade',
            'curso',
            'idade',
            ]
    dict_unidade = {}
    unidades = Unidade.objects.all()
    for unidade in unidades:
      dict_unidade[unidade.id] = unidade.nome
    CHOICES = tuple(dict_unidade.items())

    unidade = forms.ChoiceField(choices=CHOICES, required=True,)

    # dict_curso = {}
    # cursos = Curso.objects.all()
    # for curso in cursos:
    #   dict_curso[curso.id] = curso.nome
    # CHOICES = tuple(dict_curso.items())


    full_name = forms.CharField(max_length=50, 
                                required=True)
    email = forms.EmailField(required=True,
                             max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control',}))
    password = forms.CharField(max_length=8, 
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    # curso = forms.ChoiceField(choices=CHOICES,
    #                             required=True,)

    repassword = forms.CharField(max_length=8, 
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',}))
    imagem = forms.ImageField(required=False,)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")
        
        if password != repassword:
            error = "As senhas não conferem"
            self.add_error('repassword', error)
            self.add_error('password', error)

        full_name = cleaned_data.get("full_name")
        try:
            int(full_name)
            error = "Esse nome não é válido."
            self.add_error('full_name', error)
        except:
            if full_name :
                if full_name.count(" ") == 0 :
                    error = "Digite nome e sobrenome."
                    self.add_error('full_name', error)
            
            
        user = Usuario.objects.filter(email=cleaned_data.get("email"))
        if len(user) > 0:
            error = "Já existe um usuário com esse E-mail."
            self.add_error('email', error)
            
class LoginForm(forms.Form):
                                
    email = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.EmailInput({'placeholder':"E-mail"}),
    )
    
    password = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.PasswordInput({'placeholder':_("Senha")})
    )

    def cleaned_data(self):
        cleaned_data = super(LoginForm, self).clean()
        # cleaned_data.get("email")
        # self.add_error('email', "oi")

class PasswordForm(forms.Form):
                                
    email = forms.CharField(
        max_length=30,
        widget=forms.EmailInput(attrs={'autofocus': '', 'class': 'form-control', 'placeholder':"E-mail"}),
    )
    