from django.conf.urls import url
from . import views


app_name = 'core'


urlpatterns = [
    url(r'^importar-arquivo-de-vendas/$', views.ImportarArquivoVendaView.as_view(), name='importar_arquivo_de_vendas'),
]
