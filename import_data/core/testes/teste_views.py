import os
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from import_data.core.forms import ImportarArquivoForm
from import_data.core.models import Venda


class ImportarVendaViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:importar_arquivo_de_vendas'))

    def teste_get(self):
        self.assertEquals(200, self.resp.status_code)

    def teste_template(self):
        self.assertTemplateUsed(self.resp, 'core/importar_arquivo_venda.html')

    def teste_form_context(self):
        form = self.resp.context.get('form')
        self.assertIsInstance(form, ImportarArquivoForm)

    def teste_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        self.assertContains(self.resp, '<input', 3)
        self.assertContains(self.resp, 'type="file"', 1)
        self.assertContains(self.resp, 'type=\'hidden\'', 1)
        self.assertContains(self.resp, 'type="submit"', 1)


class ImportarVendaViewPostTest(TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), 'data/example_input.tab')) as f:
            self.resp = self.client.post(r('core:importar_arquivo_de_vendas'), {'arquivo': f}, follow=True)

    def teste_post(self):
        """
        Post com sucesso deve redirecionar, gravar a todos os itens do arquivo e
        informar o total importado.
        """
        self.assertRedirects(self.resp, r('core:importar_arquivo_de_vendas'))
        self.assertEquals(4, Venda.objects.count())
        self.assertContains(self.resp, 'Importação realizada. Receita Bruta Total: 95,00.')
