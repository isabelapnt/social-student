# coding:utf-8
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from core.comentario.models import Comentario
from django import forms
from django.db import IntegrityError


class CommentaryForm(forms.Form):

    descricao = forms.CharField(required=True,
                             widget=forms.TextInput({'placeholder':"Comente...s"}))

           