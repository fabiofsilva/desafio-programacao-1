import rows
from uuid import uuid4
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy as r
from django.utils.formats import number_format
from django.contrib import messages
from .forms import ImportarArquivoForm
from .models import Cliente, Comerciante, Produto, Venda


class ImportarArquivoVendaView(FormView):
    template_name = 'core/importar_arquivo_venda.html'
    form_class = ImportarArquivoForm
    success_url = r('core:importar_arquivo_de_vendas')

    def form_valid(self, form):
        registros = rows.import_from_csv(form.cleaned_data['arquivo'])
        identificador = uuid4()
        for registro in registros:
            cliente = Cliente.objects.get_or_create(nome=registro.purchaser_name)[0]
            comerciante = Comerciante.objects.get_or_create(nome=registro.merchant_name)[0]
            endereco_comerciante = comerciante.enderecos.get_or_create(endereco=registro.merchant_address)[0]
            produto = Produto.objects.get_or_create(descricao=registro.item_description)[0]

            Venda.objects.create(cliente=cliente, comerciante=comerciante, endereco_comerciante=endereco_comerciante,
                                 produto=produto, valor_unitario=registro.item_price,
                                 quantidade=registro.purchase_count, identificador=identificador)

        total = number_format(Venda.objects.receita_bruta_total(identificador))
        messages.success(self.request, f'Importação realizada. Receita Bruta Total: {total}.')
        return super().form_valid(form)
