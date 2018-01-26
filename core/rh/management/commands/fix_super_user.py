#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Basic users to manage the system'

    def handle(self, **options):
        self.stdout.write('Inicio de carregamento de dados')

        User.objects.create_superuser(
            'isabelapnt', 'isabelasouzapinto@gmail.com', 'asenhamaisdificildomundo'
        )