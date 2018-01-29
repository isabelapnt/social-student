
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.servico.models import Servico
from core.rh.models import Unidade
# from core.rh.models import *

# minimalista
class Command(BaseCommand):
    help = 'Carregamento de Servicos'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados dos Servicos')

    unidade_1 = Unidade.objects.all()[0]

    sevico_1 = Servico.objects.create(nome=u"Alguel coletivo", criado_por = "Isabela Pinto", resumo = "Aluguel coletivo", ativo=True, unidade = unidade_1)
    sevico_2 = Servico.objects.create(nome=u"Eventos", criado_por = "Ivan Machado", resumo="Serviço destinado para eventos", ativo=True, unidade = unidade_1)
    sevico_3 = Servico.objects.create(nome=u"Banco de Provas",criado_por = "Nathale Silva", resumo = "Banco de provas" , ativo=True, unidade = unidade_1)
    sevico_4 = Servico.objects.create(nome=u"Achados e Perdidos", criado_por = "Amanda Chagas", resumo = "Achados e Perdidos", ativo=True, unidade = unidade_1)
    sevico_5 = Servico.objects.create(nome=u"Estágios/Empregos", criado_por = "Nicole Andrade", resumo = "encontre vagas de emprego e estágios", ativo=True, unidade = unidade_1)


    unidade_2 = Unidade.objects.all()[1]
    sevico_1 = Servico.objects.create(nome=u"Carona Solidária",criado_por = "Nathale Silva", resumo = "Banco de provas" , ativo=True, unidade = unidade_2)
    sevico_2 = Servico.objects.create(nome=u"Achados e Perdidos", criado_por = "Amanda Chagas", resumo = "Achados e Perdidos", ativo=True, unidade = unidade_2)
    sevico_3 = Servico.objects.create(nome=u"Estágios/Empregos", criado_por = "Nicole Andrade", resumo = "encontre vagas de emprego e estágios", ativo=True, unidade = unidade_2)


    unidade_3 = Unidade.objects.all()[1]
    sevico_1 = Servico.objects.create(nome=u"Alguel coletivo", criado_por = "Isabela Pinto", resumo = "Aluguel coletivo", ativo=True, unidade = unidade_3)
    sevico_2 = Servico.objects.create(nome=u"Eventos", criado_por = "Ivan Machado", resumo="Serviço destinado para eventos", ativo=True, unidade = unidade_3)
    sevico_3 = Servico.objects.create(nome=u"Banco de Provas",criado_por = "Nathale Silva", resumo = "Banco de provas" , ativo=True, unidade = unidade_3)
    sevico_4 = Servico.objects.create(nome=u"Carona Solidária",criado_por = "Nathale Silva", resumo = "Banco de provas" , ativo=True, unidade = unidade_3)
