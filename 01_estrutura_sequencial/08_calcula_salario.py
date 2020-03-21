"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês. 
"""


def calcula_salario(valor_1_hora, valor_horas_mes):
    total_salario_mes = valor_1_hora * valor_horas_mes
    return total_salario_mes


def test_calcula_salario() -> None:
    valor_entrada_1_hora = 8
    valor_entrada_horas_por_mes = 32
    valor_esperado_total_salario_mes = (
        valor_entrada_1_hora * valor_entrada_horas_por_mes
    )
    assert (
        calcula_salario(valor_entrada_1_hora, valor_entrada_horas_por_mes)
        == valor_esperado_total_salario_mes
    )


if __name__ == "__main__":
    valor_1_hora = int(input("Informe o valor da sua hora trabalhada: "))
    valor_horas_mes = int(input("Informe o número de horas trabalhadas no mês: "))
    print(
        f"Total do seu salário nesse mês: {calcula_salario(valor_1_hora, valor_horas_mes)}"
    )
