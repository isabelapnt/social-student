# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.rh.models import *
from core.servico.models import Servico
import random
class Command(BaseCommand):
	help = 'Carregamento de Unidade'

	def handle(self, **options):
		self.stdout.write('Inicio de carregamento de dados do Unidade')

	unidades = Unidade.objects.all()
	for unidade in unidades:
		admin = Admin.objects.create(
			username="admin_" + unidade.nome,
			email="admin_" + unidade.nome + "@email.com",
			password="123",
			celular="(71)99999999",
			unidade = unidade
		)

	admin.is_staff = True
	admin.save()

	cursos = Curso.objects.all()

	for curso in cursos:
		Aluno.objects.create(
			username="aluno_" + str(curso.id),
			email="aluno_" + str(curso.id) + "@email.com",
			password="123",
			celular="(71)99999999",
			curso = curso,
			idade=22,
			unidade = curso.unidade,
			first_name = "Aluno",
			last_name = str(curso.id),
			imagem = "uploads/usuario/img/perfil.jpg"
		)
	
	# alunos = Aluno.objects.all()
	# servicos = Servico.objects.all()

	# for aluno in alunos:
	# 	index_random = random.sample(range(5,13), 6)
	# 	for i in index_random:
	# 		aluno = Servico.objects.get(id=i)
	# 		aluno.servico.add(servico)
	# 		aluno.save()