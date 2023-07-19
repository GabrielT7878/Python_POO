from dominio.servicos.calculadora_financeira import CalculadoraFinanceira

class CalculadoraJurosCompostos(CalculadoraFinanceira):
    def calcularMontanteComJuros(self, montanteInicial, periodoMeses, jurosAoMes):
        novoMontante = montanteInicial * (1 + jurosAoMes) ** periodoMeses
        return novoMontante

    def __str__(self):
        return "Calculadora de juros compostos"
