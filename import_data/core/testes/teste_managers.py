from uuid import uuid4
from django.test import TestCase
from model_mommy import mommy
from import_data.core.models import Venda


class VendaManagerTest(TestCase):
    def setUp(self):
        self.identificador = uuid4()
        mommy.make(Venda, valor_unitario=10, quantidade=3, identificador=self.identificador, _quantity=5)
        mommy.make(Venda, valor_unitario=20, quantidade=3, identificador=uuid4(), _quantity=5)

    def teste_receita_bruta_total(self):
        """Deve retornar o total da receita bruta (quantidade * valor), com base por identificador"""
        resultado = Venda.objects.receita_bruta_total(self.identificador)
        self.assertEquals(150, resultado)
