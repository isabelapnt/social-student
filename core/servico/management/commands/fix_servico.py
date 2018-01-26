
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.servico.models import Servico
# from core.rh.models import *

# minimalista
class Command(BaseCommand):
    help = 'Carregamento de Servicos'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados dos Servicos')

    # usuarios = Usuario.objects.all()

    Servico.objects.create(nome=u"Alguel coletivo", criado_por = "Isabela Pinto", resumo = "Aluguel coletivo", ativo=True)
    Servico.objects.create(nome=u"Eventos", criado_por = "Ivan Machado", resumo="Serviço destinado para eventos", ativo=True)
    Servico.objects.create(nome=u"Banco de Provas",criado_por = "Nathale Silva", resumo = "Banco de provas" , ativo=True)

    Servico.objects.create(nome=u"Achados e Perdidos", criado_por = "Amanda Chagas", resumo = "Achados e Perdidos", ativo=True)
    Servico.objects.create(nome=u"Estágios/Empregos", criado_por = "Nicole Andrade", resumo = "encontre vagas de emprego e estágios", ativo=True)