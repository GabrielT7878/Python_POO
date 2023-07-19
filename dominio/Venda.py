from dominio.pagamento.PagamentoCheque import PagamentoCheque
from dominio.pagamento.PagamentoDinheiro import PagamentoDinheiro
from dominio.pagamento.PagamentoCartao import PagamentoCartao
from datetime import datetime


from dominio.item_venda import ItemVenda

class Venda:
    def __init__(self, data):
        self.itens_venda = []
        self.esta_completa = False
        self.data = data
        self.pagamento = None

    def criar_item_venda(self, desc, quantidade):
        iv = ItemVenda(desc, quantidade)
        self.itens_venda.append(iv)

    def fazer_pagamento_dinheiro(self, quantia_fornecida):
        self.pagamento = PagamentoDinheiro(quantia_fornecida)
        return self.calcular_troco()

    def fazer_pagamento_cheque(self, quantia_fornecida, banco):
        self.pagamento = PagamentoCheque(quantia_fornecida, banco)

    def fazer_pagamento_cartao(self, quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora):
        self.pagamento = PagamentoCartao(quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora)

    def calcular_troco(self):
        return self.pagamento.get_quantia_fornecida() - self.calcular_total_venda()

    def calcular_total_venda(self):
        total_venda = 0.0
        for item_venda in self.itens_venda:
            if item_venda is not None:
                total_venda += item_venda.get_descricao_produto().get_preco() * item_venda.get_quantidade()
        return total_venda

    def set_esta_completa(self, esta_completa):
        self.esta_completa = esta_completa

    def __str__(self):
        data = datetime.now()
        status = "completa" if self.esta_completa else "incompleta"
        data_temp = f"{data.day}/{data.month}/{data.year}"
        hora_temp = f"{data.hour}:{data.minute}:{data.second}"
        cabecalho = f"Data: {data_temp} hora: {hora_temp}\n" \
                    f"\t\t\t\t\tStatus da venda: {status}\n\n" \
                    f" Descrição\t\tPreço Unitário(R$)\t\tQuantidade\t\tSubtotal(R$) \n"
        corpo = ""

        for iv in self.itens_venda:
            if iv is not None:
                corpo += str(iv)

        rodape = f"Total à vista (R$)\t\t\t\t\t\t\t{self.calcular_total_venda()}\n\n" \
                 f"{self.pagamento}\n"
        return cabecalho + corpo + rodape