"""
Exercício Python N°2:
Fazer um algoritmo que ao receber o salário atual de um funcionário,
calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
"""

print('\t ----Cálculo do novo salário ---- ')
salario_atual = float(input('Informe o salario atual: '))

if (salario_atual<500):
    salario_novo=salario_atual+(salario_atual*0.15)
    print('Salario com reajuste' '=', salario_novo)

if ((salario_atual>=500) and (salario_atual <=1000)):
    salario_novo=salario_atual+(salario_atual*0.10)
    print('Salario com reajuste' '=', salario_novo)

if (salario_atual>1000):
    salario_novo=salario_atual+(salario_atual*0.05)
    print('Salario com reajuste' '=', salario_novo)