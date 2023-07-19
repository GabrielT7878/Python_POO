from dominio.Venda import Venda
from dominio.CatalogoProdutos import CatalogoProdutos
from dominio.DescricaoProduto import DescricaoProduto
from dominio.pagamento.Operadora import Operadora
from dominio.servicos.calculadora_juros_simples import CalculadoraJurosSimples

class LocalDateTime:
    pass

class Registradora:
  def __init__(self, id):
    self.id = id
    self.vendas = []
    self.catalogo = CatalogoProdutos()

  def criar_nova_venda(self, data_hora=LocalDateTime()):  # Fornecendo um valor padrão
    venda = Venda(data_hora)  # Passando o argumento data_hora para o construtor de Venda
    self.vendas.append(venda)

  def entrar_item(self, id, quantidade):
    try:
      descricao_produto = self.catalogo.get_descricao_produto(id)
      venda = self.get_venda_corrente()
      venda.criar_item_venda(descricao_produto, quantidade)
    except DescricaoProduto as e:
      print(e)

  def finalizar_venda(self):
    self.get_venda_corrente().set_esta_completa(True)

  def fazer_pagamento(self, quantia_fornecida, operadora, quantidade_parcelas):
        return self.get_venda_corrente().fazer_pagamento_cheque(self, quantia_fornecida)

  def fazer_pagamento_banco(self, quantia_fornecida, banco):
        return self.get_venda_corrente().fazer_pagamento_banco(quantia_fornecida, banco)

  def fazer_pagamento_operadora(self, quantia_fornecida, operadora, quantidade_parcelas):
        return self.get_venda_corrente().fazer_pagamento_operadora(quantia_fornecida, operadora, quantidade_parcelas)

  def get_venda_corrente(self):
    return self.vendas[-1]

  def get_catalogo(self):
    return self.catalogo

  def set_catalogo(self, catalogo):
    self.catalogo = catalogo

  def get_id(self):
    return self.id
