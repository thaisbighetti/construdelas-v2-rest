from unittest import TestCase

from clientes.models import Clientes


class TestStringMethods(TestCase):

    def setUp(self):
        self.cliente = Clientes.objects.create(nome="Cliente", idade=20, rg="412738591", cpf="11122233345", email="cliente@gmail.com", telefone="99999-9999")

    def test_idade_isalnum(self):
        self.assertTrue(self.cliente.idade, int)


