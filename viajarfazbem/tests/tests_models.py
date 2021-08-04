from django.test import TestCase
from django.contrib.auth.models import User



""" Teste de criação um usuário, para posterior autenticação."""
class TestUser(TestCase):
    def test_setUp(self):
        self.password = '123456'
        self.my_admin = User.objects.create_superuser('thiago', 'thiago@viajarfazbem.com.br',self.password)
