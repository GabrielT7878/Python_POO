from dominio.pagamento.Pagamento import Pagamento

class PagamentoCheque(Pagamento):
    def __init__(self, quantiaFornecida, banco):
        super().__init__(quantiaFornecida)
        self.banco = banco

    def __str__(self):
        return f"Pagamento com cheque do banco {self.banco}"
