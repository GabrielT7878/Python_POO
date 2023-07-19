from dominio.pagamento.Pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self, quantiaFornecida, operadora, quantidadeParcelas, tipoCalculadora):
        super().__init__(quantiaFornecida)
        self.operadora = operadora
        self.quantidadeParcelas = quantidadeParcelas
        self.tipoCalculadora = tipoCalculadora

    def __str__(self):
        return f"Pagamento com cartão {self.operadora}, {self.quantidadeParcelas} parcelas, usando {self.tipoCalculadora}"

    def fazer_pagamento(self, quantia_fornecida):
        return 0.0  
