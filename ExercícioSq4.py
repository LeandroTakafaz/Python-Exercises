"""
Exercício Python N°4:
Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor = float(input('Informe quanto ganha por hora: '))
horas = float(input('Informe por quantas horas trabalhou: '))

salario = valor * horas

print('Seu salário esse mês é de: ',salario)