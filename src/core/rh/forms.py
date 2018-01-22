# coding:utf-8
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from core.rh.models import Aluno, Unidade, Curso
from django import forms
from django.db import IntegrityError


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Aluno

        fields = [
                'email',
                'first_name',
                'last_name',
                'unidade',
                'curso',
                'idade',
                ]
        # exclude = [
        #     "is_staff",
        # ]
        dict_unidade = {}
        unidades = Unidade.objects.all()
        for unidade in unidades:
          dict_unidade[unidade.id] = unidade.nome
        CHOICES = tuple(dict_unidade.items())

        unidade = forms.ChoiceField(choices=CHOICES, required=True,)

        dict_curso = {}
        cursos = Curso.objects.all()
        for curso in cursos:
          dict_curso[curso.id] = curso.nome
        CHOICES = tuple(dict_curso.items())

        curso = forms.ChoiceField(choices=CHOICES,
                                required=True,)
        email = forms.EmailField(required=True)

    def clean(self):

        cleaned_data = super(PerfilForm, self).clean()
        if cleaned_data.get("email") == "":
            self.add_error("email", ValidationError('Campo e-mail é obrigatório'))
        if cleaned_data.get("unidade") == "":
            self.add_error("unidade", ValidationError('Campo unidade é obrigatório'))
        if cleaned_data.get("curso") == "":
            self.add_error("curso", ValidationError('Campo curso é obrigatório'))