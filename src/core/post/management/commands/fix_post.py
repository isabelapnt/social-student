
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from core.servico.models import Servico
from core.rh.models import *
from core.post.models import Post
from core.comentario.models import Comentario
# minimalista
class Command(BaseCommand):
    help = 'Carregamento de Post'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados dos Post')

    Aluguel = Servico.objects.get(nome="Alguel coletivo")
    Eventos = Servico.objects.get(nome="Eventos")
    Banco_prova = Servico.objects.get(nome="Banco de Provas")
    Achados_Perdidos = Servico.objects.get(nome="Achados e Perdidos")
    Vagas = Servico.objects.get(nome=u"Estágios/Empregos")
    
    usuario = Usuario.objects.all()[11]

    #Aluguel

    post_1 = Post.objects.create(titulo = "Casa em Villas", servico = Aluguel, conteudo= "Vaga para meninas, quarto compartilhado, duas pessoas. R$ 340, na frente do porto da barra, ap e quarto com mobília completa. Ponto de ônibus próximo. Valor não inclui despesas (água, luz, net). Primeiro mês taxa de R$ 200 pro caução.", criado_por = usuario)

    post_2 = Post.objects.create(titulo = "QUARTO INDIVIDUAL PARA MENINA EM APARTAMENTO NA ONDINA", servico = Aluguel, conteudo= "Quarto de dependência, porém, sem mobília. Apartamento de dois quartos e dependência (2 moradoras) amplo, arejado, mobiliado e organizado. Valor: R$400 + energia e internet", criado_por = usuario)
    
    post_3 = Post.objects.create(titulo = "Aluga_se casa 2/4 suíte área de serviço cozinha", servico = Aluguel, conteudo= "Perto de ponto de ônibus, Farmácia, Mercado, Escola, Açougue, Igreja Panificadora etc... CabulaVII Tancredo Neves Próximo Condomínio Árvoredo. Contatos: 97810-8964/ 99224-5742 Zap", criado_por = usuario)

    Comentario.objects.create(usuario = usuario, post = post_1, descricao = "Olá tenho interesse.")

    Comentario.objects.create(usuario = usuario, post = post_2, descricao = "Você pode dar mais informação.")
    
    Comentario.objects.create(usuario = usuario, post = post_3, descricao = "Oii, tenho interesse.")

    #Eventos

    post_4 = Post.objects.create(titulo = "Trote de Fámacia", servico = Eventos, conteudo= "Vocês vão adorar o que estamos preparando para vocês! Calmaaaaaaa Calouro, nada de tinta por enquanto! Fiquem tranquilos, quando chegar a hora vocês saberão!", criado_por = usuario)

    post_5 = Post.objects.create(titulo = "Trote de Administração", servico = Eventos, conteudo= "Vocês vão adorar o que estamos preparando para vocês! Calmaaaaaaa Calouro, nada de tinta por enquanto! Fiquem tranquilos, quando chegar a hora vocês saberão!", criado_por = usuario)

    post_6 = Post.objects.create(titulo = "Trote de Biologia", servico = Eventos, conteudo= "Vocês vão adorar o que estamos preparando para vocês! Calmaaaaaaa Calouro, nada de tinta por enquanto! Fiquem tranquilos, quando chegar a hora vocês saberão!", criado_por = usuario)

    Comentario.objects.create(usuario = usuario, post = post_4, descricao = "Não vou perderrrrrr.")

    Comentario.objects.create(usuario = usuario, post = post_5, descricao = "Melhor trote da UFBA.")
    
    Comentario.objects.create(usuario = usuario, post = post_6, descricao = "Chega logo")

    #Banco_prova

    post_7 = Post.objects.create(titulo = "Prova de Grafos III Unidade", servico = Banco_prova, conteudo= "Link em Anexo", criado_por = usuario)

    post_8 = Post.objects.create(titulo = "Prova de Engenharia de Software", servico = Banco_prova, conteudo= "Link em Anexo", criado_por = usuario)

    post_9 = Post.objects.create(titulo = "Prova de Biologia", servico = Banco_prova, conteudo= "Link em Anexo", criado_por = usuario)

    Comentario.objects.create(usuario = usuario, post = post_7, descricao = "voxê tem a prova da  segunda unidade?.")

    Comentario.objects.create(usuario = usuario, post = post_8, descricao = "Salvou minha vida!!!!.")
    
    Comentario.objects.create(usuario = usuario, post = post_9, descricao = "Você tem prova do professora Rafael??")
    
    #Achados_Perdidos

    post_10 = Post.objects.create(titulo = "iPhone 5S Rosa", servico = Achados_Perdidos, conteudo= "Pessoal encontrei este celular no proximo ao correio de instituto de matémática, se alguém conhece o dono por favor avisem!", criado_por = usuario)

    post_11 = Post.objects.create(titulo = "Guarda-Chuva", servico = Achados_Perdidos, conteudo= "Pessoal encontrei este guarda chuva no proximo ao correio de instituto de Física, se alguém conhece o dono por favor avisem!", criado_por = usuario)

    post_12 = Post.objects.create(titulo = "Mochila", servico = Achados_Perdidos, conteudo= "Pessoal encontrei este Mochila no proximo ao correio de instituto de Biologia, se alguém conhece o dono por favor avisem!", criado_por = usuario)

    Comentario.objects.create(usuario = usuario, post = post_10, descricao = "Eu conheço a dona, Adriele Cardoso")

    Comentario.objects.create(usuario = usuario, post = post_11, descricao = "Se não achar o dono eu quero, rs.")
    
    Comentario.objects.create(usuario = usuario, post = post_12, descricao = "Eu conheço o dono, Fabio Costa de Física.")

    #Vagas

    post_13 = Post.objects.create(titulo = "Vaga para Professor", servico = Vagas, conteudo= "Vagas disponíveis para seleção de professores nas mediações de Itapua, são Cristóvão , boca do rio. De preferência com magistério cursando pedagogia!", criado_por = usuario)

    post_14 = Post.objects.create(titulo = "Desenvolvedor Web", servico = Vagas, conteudo= "Requisitos: Python, Django, JavaScript, HTML, CSS; Interessados: vaga@email.com ", criado_por = usuario)

    post_15 = Post.objects.create(titulo = "VAGA URGENTE!!", servico = Vagas, conteudo= "PRECISA-SE DE ESTUDANTES DE ENFERMAGEM; NECESSÁRIO TER CNH; CURSADO PERÍODO NOTURNO;", criado_por = usuario),

    Comentario.objects.create(usuario = usuario, post = post_13, descricao = "Tem mais informações?")

    Comentario.objects.create(usuario = usuario, post = post_14, descricao = "Sabe quanto pretendem pagar?")
    
    # Comentario.objects.create(usuario = usuario, post = post_15, descricao = "Opa, queeeero!")