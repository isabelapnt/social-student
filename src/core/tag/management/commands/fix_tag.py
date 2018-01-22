
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.tag.models import Tags
# minimalista
class Command(BaseCommand):
    help = 'Carregamento de Tags'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados do Tags')

    Tags.objects.create(nome = "prova")
    Tags.objects.create(nome = "teste")
    Tags.objects.create(nome = "ajuda")

    Tags.objects.create(nome = "eventos")
    Tags.objects.create(nome = "festa")
    Tags.objects.create(nome = u"música")
    Tags.objects.create(nome = u"dança")
    
    Tags.objects.create(nome = "apartamento")
    Tags.objects.create(nome = "casa")
    Tags.objects.create(nome = "aluguel")
    Tags.objects.create(nome = "compartilhar")
    Tags.objects.create(nome = "moradia")
    Tags.objects.create(nome = "facilidade")
    Tags.objects.create(nome = "comodidade")
    Tags.objects.create(nome = u"república")
   
    Tags.objects.create(nome = "emprego")
    Tags.objects.create(nome = u"estágio")
    Tags.objects.create(nome = "vagas")
    Tags.objects.create(nome = "trabalho")
    Tags.objects.create(nome = "dinheiro")
    Tags.objects.create(nome = u"experiência")

    Tags.objects.create(nome = "busca")
    Tags.objects.create(nome = "procura")
    Tags.objects.create(nome = "semestre")