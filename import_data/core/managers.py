from django.db.models import QuerySet, Sum, F


class VendaQuerySet(QuerySet):
    def receita_bruta_total(self, identificador):
        resultado = self.filter(identificador=identificador).aggregate(total=Sum(F('valor_unitario') * F('quantidade')))
        return resultado.get('total')
