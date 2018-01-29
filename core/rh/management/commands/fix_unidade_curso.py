
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.rh.models import Unidade, Curso
# minimalista
class Command(BaseCommand):
    help = 'Carregamento de Unidade'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados do Unidade')

    unidade_1 = Unidade.objects.create(
        nome="UFBA",
        telefone="87878787878",
        endereco = "Ademar deAbarros",
        bairro = "Ondina",
        cidade = "Salvador",
        estado = "Bahia",
        pais = "Brasil")


    unidade_2 = Unidade.objects.create(
        nome="UNEB",
        telefone="87878787878",
        endereco = "Olando souza",
        bairro = "Cabula",
        cidade = "Salvador",
        estado = "Bahia",
        pais = "Brasil")

    unidade_3 = Unidade.objects.create(
        nome="UFRB",
        telefone="87878787878",
        endereco = "Eufrozina Miranda",
        bairro = "Tento",
        cidade = "Cruz das Almas",
        estado = "Bahia",
        pais = "Brasil")

    Curso.objects.create(nome=u"Ciência da Compuatação", unidade=unidade_1)
    Curso.objects.create(nome=u"Sistema da informação", unidade=unidade_1)
    Curso.objects.create(nome=u"Engenharia da Computação", unidade=unidade_1)

    Curso.objects.create(nome=u"Ciência da Compuatação", unidade=unidade_2)
    Curso.objects.create(nome=u"Sistema da informação", unidade=unidade_2)
    Curso.objects.create(nome=u"Engenharia da Computação", unidade=unidade_2)

    Curso.objects.create(nome=u"Ciência da Compuatação", unidade=unidade_3)
    Curso.objects.create(nome=u"Sistema da informação", unidade=unidade_3)
    Curso.objects.create(nome=u"Engenharia da Computação", unidade=unidade_3)