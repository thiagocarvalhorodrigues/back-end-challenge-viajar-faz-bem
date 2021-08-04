from django.test import TestCase
from django.contrib.auth.models import User
# from viajarfazbem.api.models import Country


""" Teste de criação um usuário, para posterior autenticação."""
class TestStudent(TestCase):
    def test_setUp(self):
        self.password = '123456'
        self.my_admin = User.objects.create_superuser('thiago', 'thiago@viajarfazbem.com.br',self.password)
#
#
# """ Cria um país, e """
# class CountryTestCase(TestCase):
#     def test_setUp(self):
#         Country.objects.create(
#             name='Portugal',
#             slug='portugal',
#         )
#
#     def test_retorno_str(self):
#         pais = Country.objects.get(name='Portugal')
#         self.assertEquals(pais.__str__(),'Portugal')
