from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import VendaQuerySet


class Cliente(models.Model):
    nome = models.CharField(verbose_name=_('Nome'), max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Comerciante(models.Model):
    nome = models.CharField(verbose_name=_('Nome'), max_length=100, unique=True)

    def __str__(self):
        return self.nome


class EnderecoComerciante(models.Model):
    comerciante = models.ForeignKey(Comerciante, related_name='enderecos')
    endereco = models.CharField(verbose_name=_('Endereço'), max_length=255)

    class Meta:
        unique_together = ('comerciante', 'endereco')

    def __str__(self):
        return self.endereco


class Produto(models.Model):
    descricao = models.CharField(verbose_name=_('Descrição'), max_length=100, unique=True)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='compras')
    comerciante = models.ForeignKey(Comerciante, related_name='vendas')
    endereco_comerciante = models.ForeignKey(EnderecoComerciante)
    produto = models.ForeignKey(Produto, related_name='vendas')
    valor_unitario = models.DecimalField(verbose_name=_('Valor Unitário'), max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(verbose_name=_('Quantidade'))
    identificador = models.CharField(max_length=32)

    objects = VendaQuerySet.as_manager()
