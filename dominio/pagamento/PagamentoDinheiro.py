from dominio.pagamento.Pagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def __str__(self):
        return ("Pagamento em dinheiro")
