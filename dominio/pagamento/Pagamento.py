
class Pagamento:
    def __init__(self, quantia_fornecida):
        self.quantia_fornecida = quantia_fornecida

    def get_quantia_fornecida(self):
        return self.quantia_fornecida

    def fazer_pagamento(self, quantia_fornecida):
        return 0.0

    def __str__(self):
        return f"Pagamento de R$ {self.quantia_fornecida:.2f}"
