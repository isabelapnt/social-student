# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from core.tag.models import Tags

class ServicoForm(forms.Form):

    nome = forms.CharField(max_length=50, required=True)
    resumo = forms.CharField(widget=forms.Textarea(),required=True)
    dict_tag = {}
    
    # tags = Tags.objects.all()
    # for tag in tags:
    #       dict_tag[tag.id] = tag.nome
    # CHOICES = tuple(dict_tag.items())
    # tags = forms.ChoiceField(choices=CHOICES)

    CHOICES = [('select1','select 1'),
         ('select2','select 2')]
    has_carrosel = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    CHOICES = [('select1','select 1'),
         ('select2','select 2')]
    has_anexo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     password = cleaned_data.get("password")
    #     repassword = cleaned_data.get("repassword")
        
    #     if password != repassword:
    #         error = "As senhas não conferem"
    #         self.add_error('repassword', error)
            
            

    