# coding:utf-8
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from core.rh.models import Aluno, Unidade, Curso
from django import forms
from django.db import IntegrityError

class PerfilForm(forms.Form):
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


    # full_name = forms.CharField(max_length=50, 
    #                             required=True)
    # email = forms.EmailField(required=True,
    #                          max_length=50,
    #                          widget=forms.EmailInput(attrs={'class': 'form-control',}))
    password = forms.CharField(max_length=8, 
                                required=False,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    # curso = forms.ChoiceField(choices=CHOICES,
    #                             required=True,)

    repassword = forms.CharField(max_length=8,
                                required=False,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',}))
    imagem = forms.ImageField(required=False,)

    def clean(self):
        cleaned_data = super(PerfilForm, self).clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")
        
        if len(password) != 0 and len(repassword) != 0:
            if password != repassword:
                error = "As senhas não conferem"
                self.add_error('repassword', error)
                self.add_error('password', error)
                raise forms.ValidationError(u"As senhas não conferem")
        

class RecoverForm(forms.ModelForm):

    class Meta:
        model = Aluno

        fields = [
                'email',
                ]

    email = forms.EmailField(required=True,
                             max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':"E-mail"}))
    def clean(self):

        cleaned_data = super(RecoverForm, self).clean()
        if cleaned_data.get("email") == "":
            error = "Campo e-mail é obrigatório."
            self.add_error('email', error)
        if not Aluno.objects.filter(email = cleaned_data.get("email")):
            error = "Não há usuário cadastrado com esse email."
            self.add_error('email', error)      

           