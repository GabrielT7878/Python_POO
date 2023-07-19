from dominio.servicos.calculadora_juros_compostos import CalculadoraJurosCompostos
from dominio.servicos.calculadora_juros_simples import CalculadoraJurosSimples

def main():
    montante_inicial = 10000
    periodo_meses = 3
    juros_ao_mes = 0.05

    calculadora = CalculadoraJurosCompostos()
    print("************* Cálculo de juros com calculadora de juros compostos **********************")
    print("Montante inicial..:", montante_inicial)
    print("Período em meses...:", periodo_meses)
    print("Juros ao mês......:", juros_ao_mes)
    print("Objeto calculadora..:", calculadora)
    print("Total..:", calculadora.calcular_montante_com_juros(montante_inicial, periodo_meses, juros_ao_mes))
    print("*****************************************************")

    calculadora = CalculadoraJurosSimples()
    print("************* Cálculo de juros com calculadora de juros simples **********************")
    print("Montante inicial..:", montante_inicial)
    print("Período em meses...:", periodo_meses)
    print("Juros ao mês......:", juros_ao_mes)
    print("Objeto calculadora..:", calculadora)
    print("Total..:", calculadora.calcular_montante_com_juros(montante_inicial, periodo_meses, juros_ao_mes))
    print("*****************************************************")

if __name__ == "__main__":
    main()